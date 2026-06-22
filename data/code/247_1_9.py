class NumberAdder:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    adder = NumberAdder()
    result1 = adder.add(5, 3)
    print(result1)
    result2 = adder.add(-10, 20)
    print(result2)