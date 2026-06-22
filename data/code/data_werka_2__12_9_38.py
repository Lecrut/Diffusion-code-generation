class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = ratios

    def validate_ratios(self):
        if not all(isinstance(ratio, (int, float)) and ratio >= 0 for ratio in self.ratios):
            raise ValueError("All ratios must be non-negative numbers.")
        if sum(self.ratios) == 0:
            raise ValueError("Total ratio cannot be zero.")

    def normalize(self):
        self.validate_ratios()
        total_ratio = sum(self.ratios)
        return [ratio / total_ratio for ratio in self.ratios]

if __name__ == '__main__':
    sample_ratios = [4, 6, 8]
    converter = WeightRatioConverter(sample_ratios)
    try:
        normalized_weights = converter.normalize()
        print(normalized_weights)
    except ValueError as e:
        print(e)