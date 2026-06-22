class IntegerAdder:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    adder = IntegerAdder()
    result1 = adder.add(3, 5)
    print(result1)
    result2 = adder.add(-10, 20)
    print(result2)