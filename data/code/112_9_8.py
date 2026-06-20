class NumericAdder:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    result = NumericAdder.add(num1, num2)
    print(result)