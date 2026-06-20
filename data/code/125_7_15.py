class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    calc = BasicCalculator()
    print("Addition Result:", calc.add(5, 3))
    print("Subtraction Result:", calc.subtract(10, 4))