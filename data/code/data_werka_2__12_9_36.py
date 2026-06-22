class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = self.validate_ratios(ratios)

    @staticmethod
    def validate_ratios(ratios):
        if not all(isinstance(ratio, (int, float)) and ratio >= 0 for ratio in ratios):
            raise ValueError("All ratios must be non-negative numbers.")
        return ratios

    def normalize(self):
        total_ratio = sum(self.ratios)
        if total_ratio == 0:
            raise ValueError("Total ratio cannot be zero.")
        normalized_weights = [ratio / total_ratio for ratio in self.ratios]
        return normalized_weights

if __name__ == '__main__':
    sample_ratios = [1, 2, 3, 4]
    converter = WeightRatioConverter(sample_ratios)
    normalized_distribution = converter.normalize()
    print(normalized_distribution)