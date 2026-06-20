import math

class FloatingPointAccumulator:
    def __init__(self):
        self.values = []

    def add(self, value):
        if not isinstance(value, float):
            raise ValueError("Only floating-point values are allowed")
        self.values.append(value)

    def calculate_sum(self):
        return math.fsum(self.values)

if __name__ == '__main__':
    accumulator = FloatingPointAccumulator()
    accumulator.add(0.1)
    accumulator.add(0.2)
    accumulator.add(0.3)
    total = accumulator.calculate_sum()
    print(total)