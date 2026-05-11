class FruitColorPair:
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color
    def __str__(self):
        return f"{self.fruit} is {self.color}"
if __name__ == '__main__':
    pair1 = FruitColorPair("Apple", "Red")
    pair2 = FruitColorPair("Banana", "Yellow")
    pair3 = FruitColorPair("Grape", "Purple")
    print(pair1)
    print(pair2)
    print(pair3)