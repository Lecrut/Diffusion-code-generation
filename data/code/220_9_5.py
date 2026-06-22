class TupleAverageCalculator:
    def __init__(self, tuples):
        self.tuples = tuples

    def calculate_average(self):
        total = sum(sum(t) for t in self.tuples)
        count = sum(len(t) for t in self.tuples)
        return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5,))
    calculator = TupleAverageCalculator(sample_data)
    print(calculator.calculate_average())