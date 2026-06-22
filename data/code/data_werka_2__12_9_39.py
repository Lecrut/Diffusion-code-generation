class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = ratios

    def normalize_ratios(self):
        total = sum(self.ratios)
        if total == 0:
            raise ValueError("Total of ratios must not be zero")
        return [ratio / total for ratio in self.ratios]

if __name__ == '__main__':
    sample_ratios = [2, 3, 5]
    converter = WeightRatioConverter(sample_ratios)
    normalized_weights = converter.normalize_ratios()
    print(normalized_weights)