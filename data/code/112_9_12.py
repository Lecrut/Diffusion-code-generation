class NumericAdder:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    result = NumericAdder.add(7, 8)
    print(result)