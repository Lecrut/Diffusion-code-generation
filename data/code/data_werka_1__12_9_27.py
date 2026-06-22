class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = ratios

    def normalize(self):
        total_ratio = sum(self.ratios)
        normalized_weights = [ratio / total_ratio for ratio in self.ratios]
        return normalized_weights

if __name__ == '__main__':
    sample_ratios = [10, 20, 30, 40]
    converter = WeightRatioConverter(sample_ratios)
    normalized_distribution = converter.normalize()
    print(normalized_distribution)