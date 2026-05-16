class FruitColorPair:
    def __init__(self, fruit, color):
        self.fruit = fruit
        self.color = color
    def __str__(self):
        return f"{self.fruit} is {self.color}"
if __name__ == '__main__':
    fruit1 = "Apple"
    color1 = "Red"
    pair1 = FruitColorPair(fruit1, color1)
    print(pair1)
    fruit2 = "Banana"
    color2 = "Yellow"
    pair2 = FruitColorPair(fruit2, color2)
    print(pair2)