class FruitCycler:
    def __init__(self, fruits):
        self.fruits = fruits

    def cycle_fruits(self):
        for fruit in self.fruits:
            yield fruit.upper()

if __name__ == '__main__':
    cycler = FruitCycler(['apple', 'banana', 'cherry'])
    print("Fruits in uppercase:")
    for fruit in cycler.cycle_fruits():
        print(fruit)