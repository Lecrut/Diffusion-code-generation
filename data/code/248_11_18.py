class FloatAdder:
    def add(self, a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    adder = FloatAdder()
    result1 = adder.add(3.141592653589793, 2.718281828459045)
    result2 = adder.add(0.0000000001, 0.0000000002)
    print(result1)
    print(result2)