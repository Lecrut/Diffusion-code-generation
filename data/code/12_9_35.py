class WeightRatioConverter:
    def __init__(self, ratios):
        self.ratios = ratios

    def normalize(self):
        if not self.ratios:
            raise ValueError("Ratios list cannot be empty.")
        
        total_ratio = sum(self.ratios)
        if total_ratio == 0:
            raise ValueError("Total ratio cannot be zero.")
        
        return [ratio / total_ratio for ratio in self.ratios]

    def convert_to_weights(self):
        normalized_ratios = self.normalize()
        max_ratio = max(normalized_ratios)
        return [max_ratio * ratio for ratio in normalized_ratios]

if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    converter = WeightRatioConverter(sample_ratios)

    print("Normalized Weights:")
    print(converter.normalize())

    print("\nConverted to Weights:")
    print(converter.convert_to_weights())