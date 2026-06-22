class NumberAdder:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    calculator = NumberAdder()
    result1 = calculator.add(3, 5)
    result2 = calculator.add(7, 9)
    print(result1)
    print(result2)