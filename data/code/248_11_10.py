class PreciseAdder:
    def add(self, a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    adder = PreciseAdder()
    result1 = adder.add(3.141592653589793, 2.718281828459045)
    result2 = adder.add(1.0, 2.0)
    print(result1)
    print(result2)