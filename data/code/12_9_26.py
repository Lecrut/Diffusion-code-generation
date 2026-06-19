class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = ratios

    def normalize_ratios(self):
        total_sum = sum(self.ratios)
        if total_sum == 0:
            return [0.0] * len(self.ratios)
        return [ratio / total_sum for ratio in self.ratios]

if __name__ == '__main__':
    sample_ratios = [2, 3, 5]
    converter = WeightRatioConverter(sample_ratios)
    normalized_weights = converter.normalize_ratios()
    print(normalized_weights)