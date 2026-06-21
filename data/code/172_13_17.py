class KeyValueMapper:
    def __init__(self):
        self.mapping = {1: 'one', 2: 'two', 3: 'three'}

    def get_value(self, key):
        return self.mapping.get(key, "Key not found")

if __name__ == '__main__':
    mapper = KeyValueMapper()
    print(mapper.get_value(1))
    print(mapper.get_value(2))
    print(mapper.get_value(4))