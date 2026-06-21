class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = ratios

    def normalize(self):
        total_ratio = sum(self.ratios)
        if total_ratio == 0:
            raise ValueError("Total ratio cannot be zero.")
        normalized_weights = [ratio / total_ratio for ratio in self.ratios]
        return normalized_weights

if __name__ == '__main__':
    sample_ratios = [1, 2, 3, 4]
    converter = WeightRatioConverter(sample_ratios)
    try:
        normalized_distribution = converter.normalize()
        print(normalized_distribution)
    except ValueError as e:
        print(e)