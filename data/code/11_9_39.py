class RatioCalculator:
    def __init__(self, length_pairs):
        self.length_pairs = length_pairs

    def calculate_ratios(self):
        ratios = []
        for length1, length2 in self.length_pairs:
            if length2 != 0:
                ratio = length1 / length2
                ratios.append(ratio)
        return ratios

if __name__ == '__main__':
    sample_length_pairs = [(10, 2), (5, 0), (8, 4), (3, 3)]
    calculator = RatioCalculator(sample_length_pairs)
    result = calculator.calculate_ratios()
    print(result)