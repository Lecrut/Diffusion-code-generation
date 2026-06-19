class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = ratios

    def normalize_weights(self):
        total_ratio = sum(self.ratios)
        normalized_ratios = [ratio / total_ratio for ratio in self.ratios]
        return normalized_ratios

if __name__ == '__main__':
    sample_ratios = [10, 20, 30, 40]
    converter = WeightRatioConverter(sample_ratios)
    print(converter.normalize_weights())