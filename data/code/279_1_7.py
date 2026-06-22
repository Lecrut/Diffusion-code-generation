class FruitCycler:
    def __init__(self, fruits):
        self.fruits = fruits
        self.index = 0

    def get_next_fruit(self):
        if self.index >= len(self.fruits):
            self.index = 0
        fruit = self.fruits[self.index]
        self.index += 1
        return fruit.upper()

if __name__ == '__main__':
    cycler = FruitCycler(['apple', 'banana', 'cherry'])
    print(cycler.get_next_fruit())
    print(cycler.get_next_fruit())
    print(cycler.get_next_fruit())
    print(cycler.get_next_fruit())