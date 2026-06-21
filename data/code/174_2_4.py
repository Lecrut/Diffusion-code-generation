class KeyValueConverter:
    def __init__(self):
        self.data = {}

    def add_pair(self, key, value):
        self.data[key] = value

    def get_dict(self):
        return self.data.copy()

if __name__ == '__main__':
    converter = KeyValueConverter()
    converter.add_pair("Alice", 30)
    converter.add_pair("Bob", 25)
    converter.add_pair("Charlie", 35)
    converter.add_pair("Bob", 40)

    final_dict = converter.get_dict()
    print(final_dict)