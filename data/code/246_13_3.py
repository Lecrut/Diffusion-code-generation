class DecimalAdder:
    def __init__(self, value1: float, value2: float):
        self.value1 = value1
        self.value2 = value2

    def add(self) -> float:
        return self.value1 + self.value2

if __name__ == '__main__':
    calculator = DecimalAdder(3.5, 2.1)
    result = calculator.add()
    print(result)