class WeightRatioConverter:
    def __init__(self, weight_ratios):
        self.weight_ratios = weight_ratios

    def normalize(self):
        total_ratio = sum(self.weight_ratios)
        return [ratio / total_ratio for ratio in self.weight_ratios]

if __name__ == '__main__':
    sample_weights = [2, 3, 5]
    converter = WeightRatioConverter(sample_weights)
    normalized_weights = converter.normalize()
    print(normalized_weights)