class PreciseCalculator:
    def add_numbers(self, a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    calc = PreciseCalculator()
    result = calc.add_numbers(0.1, 0.2)
    print(result)