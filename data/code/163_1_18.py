class FruitColorPair:
    def __init__(self):
        self.pairs = []

    def add_pair(self, fruit, color):
        self.pairs.append((fruit, color))

    def get_pairs(self):
        return self.pairs

if __name__ == '__main__':
    fruit_color_instance = FruitColorPair()
    fruit_color_instance.add_pair("apple", "red")
    fruit_color_instance.add_pair("banana", "yellow")
    fruit_color_instance.add_pair("cherry", "red")
    fruit_color_instance.add_pair("date", "brown")
    print(fruit_color_instance.get_pairs())