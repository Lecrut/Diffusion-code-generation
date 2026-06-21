class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = ratios

    def normalize(self):
        total = sum(self.ratios)
        if total == 0:
            raise ValueError("Total ratio cannot be zero.")
        return [ratio / total for ratio in self.ratios]

if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    converter = WeightRatioConverter(sample_ratios)
    normalized_weights = converter.normalize()
    print(normalized_weights)