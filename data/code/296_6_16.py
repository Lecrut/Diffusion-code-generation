class HarmonicMeanCalculator:
    def __init__(self, ratios):
        self.ratios = ratios

    def calculate_harmonic_mean(self):
        if not self.ratios or len(self.ratios) != 3:
            raise ValueError("Ratios must contain exactly three elements.")
        
        sum_of_reciprocals = sum(1 / ratio[0] for ratio in self.ratios)
        harmonic_mean = 3 / sum_of_reciprocals
        return harmonic_mean

if __name__ == '__main__':
    sample_ratios = [(2, 3), (4, 5), (6, 7)]
    calculator = HarmonicMeanCalculator(sample_ratios)
    result = calculator.calculate_harmonic_mean()
    print(result)