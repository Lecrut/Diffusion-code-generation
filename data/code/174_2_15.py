class KeyValueDict:
    def __init__(self):
        self.data = {}

    def add_pair(self, key, value):
        self.data[key] = value

    def get_dict(self):
        return self.data

if __name__ == '__main__':
    kv_dict = KeyValueDict()
    pairs = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Bob", 40)]
    for key, value in pairs:
        kv_dict.add_pair(key, value)
    result_dict = kv_dict.get_dict()
    print(result_dict)