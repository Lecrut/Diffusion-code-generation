class FruitColorPairs:
    def __init__(self):
        self.pairs = [
            ("apple", "red"),
            ("banana", "yellow"),
            ("cherry", "red"),
            ("date", "brown")
        ]

    def get_pairs(self):
        return self.pairs

if __name__ == '__main__':
    fruit_color_instance = FruitColorPairs()
    pairs = fruit_color_instance.get_pairs()
    print(pairs)