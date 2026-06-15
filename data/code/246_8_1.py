class Adder:
    def __init__(self):
        pass
    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    calculator = Adder()
    result = calculator.add(5, 3)
    print(result)