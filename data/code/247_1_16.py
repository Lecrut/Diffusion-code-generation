class NumberAdder:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calculator = NumberAdder()
    result1 = calculator.add(5, 3)
    print(result1)
    result2 = calculator.add(-10, 20)
    print(result2)