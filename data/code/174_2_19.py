class DictConverter:
    def __init__(self):
        self.result = {}

    def add_pairs(self, pairs):
        for key, value in pairs:
            self.result[key] = value

if __name__ == '__main__':
    converter = DictConverter()
    converter.add_pairs([("Alice", 30), ("Bob", 25), ("Charlie", 35)])
    converter.add_pairs([("Bob", 40), ("David", 28)])
    print(converter.result)