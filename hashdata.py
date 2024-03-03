class HashData:
    def __init__(self, number):
        self.number = number
        self.datalist = [[] for _ in range(number)]

    def _hash(self, key):
        return hash(key) % self.number

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.datalist[index]:
            if pair[0] == key:
                pair[1] = value  # Update value if key already exists
                return
        self.datalist[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.datalist[index]:
            if pair[0] == key:
                return pair[1]  # Return value associated with the key
        raise KeyError("Key not found")

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.datalist[index]):
            if pair[0] == key:
                del self.datalist[index][i]  # Remove key-value pair
                return
        raise KeyError("Key not found")

#test the function
hash_data=HashData(10)
hash_data.insert("apples", 5)
hash_data.insert("banana", 7)
hash_data.insert("orange", 3)