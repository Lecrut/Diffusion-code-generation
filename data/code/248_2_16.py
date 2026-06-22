class IntegerAdder:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def add(self) -> int:
        return self.num1 + self.num2

if __name__ == '__main__':
    adder_instance = IntegerAdder(7, 8)
    result = adder_instance.add()
    print(result)