class TupleAverager:
    def __init__(self, tuple1, tuple2):
        self.tuple1 = tuple1
        self.tuple2 = tuple2

    def calculate_averages(self):
        if len(self.tuple1) != len(self.tuple2):
            raise ValueError("Tuples must have the same length.")
        return tuple((a + b) / 2 for a, b in zip(self.tuple1, self.tuple2))

if __name__ == '__main__':
    averager = TupleAverager((10, 20, 30), (40, 50, 60))
    try:
        result = averager.calculate_averages()
        print(result)
    except ValueError as e:
        print(e)