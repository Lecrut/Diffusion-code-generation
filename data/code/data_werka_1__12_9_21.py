class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = ratios

    def normalize(self):
        total_ratio = sum(self.ratios)
        if total_ratio == 0:
            raise ValueError("Total ratio cannot be zero.")
        return [ratio / total_ratio for ratio in self.ratios]

if __name__ == '__main__':
    sample_ratios = [2, 3, 5]
    converter = WeightRatioConverter(sample_ratios)
    normalized_weights = converter.normalize()
    print(normalized_weights)