class FruitColorPairs:
    def __init__(self):
        self.fruits = ["apple", "banana", "cherry"]
        self.colors = ["red", "yellow", "red"]

    def get_pairs(self):
        return list(zip(self.fruits, self.colors))

if __name__ == '__main__':
    fruit_color_pairs_instance = FruitColorPairs()
    pairs = fruit_color_pairs_instance.get_pairs()
    print(pairs)