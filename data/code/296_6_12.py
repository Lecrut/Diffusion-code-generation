class HarmonicMeanCalculator:
    def __init__(self, ratios):
        self.ratios = ratios

    def calculate_harmonic_mean(self):
        total = 0.0
        for numerator, denominator in self.ratios:
            if denominator != 0:
                total += numerator / denominator
            else:
                raise ValueError("Denominator cannot be zero")
        return len(self.ratios) / total if total != 0 else float('inf')

if __name__ == '__main__':
    sample_ratios = [(1, 2), (3, 4), (5, 6)]
    calculator = HarmonicMeanCalculator(sample_ratios)
    result = calculator.calculate_harmonic_mean()
    print(result)