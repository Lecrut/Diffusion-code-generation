class FactorialEngine:
    def calculate(self, value):
        if value < 0:
            raise ValueError("Negative input")
        result = 1
        for factor in range(2, value + 1):
            result *= factor
        return result

if __name__ == '__main__':
    engine = FactorialEngine()
    samples = [0, 1, 5, 12]
    for n in samples:
        print(engine.calculate(n))