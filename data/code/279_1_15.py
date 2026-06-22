class FruitCycler:
    FRUITS = ['apple', 'banana', 'cherry']

    @staticmethod
    def cycle_fruits():
        for fruit in FruitCycler.FRUITS:
            yield fruit.upper()

if __name__ == '__main__':
    for fruit in FruitCycler.cycle_fruits():
        print(fruit)