class PairAverageCalculator:
    @staticmethod
    def calculate_average(a, b):
        return (a + b) / 2

    @classmethod
    def process_pairs(cls, pairs):
        for pair in pairs:
            if not isinstance(pair, (list, tuple)) or len(pair) != 2 or not all(isinstance(x, (int, float)) for x in pair):
                raise ValueError("All pairs must contain exactly two numbers.")
        return tuple(cls.calculate_average(a, b) for a, b in pairs)

if __name__ == '__main__':
    sample_data_valid = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    result = PairAverageCalculator.process_pairs(sample_data_valid)
    print(result)