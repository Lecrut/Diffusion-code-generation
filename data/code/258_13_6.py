class TupleAverageCalculator:
    def average_pairs(self, tuple1, tuple2):
        return tuple((a + b) / 2 for a, b in zip(tuple1, tuple2))

if __name__ == '__main__':
    calculator = TupleAverageCalculator()
    result = calculator.average_pairs((10, 20, 30), (40, 50, 60))
    print(result)