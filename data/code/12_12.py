class WeightRatioConverter:
    def convert_to_normalized_distribution(self, ratios):
        if not ratios:
            return {}
        total = sum(ratios)
        if total == 0:
            return {ratio: 0.0 for ratio in ratios}
        normalized_distribution = {}
        for ratio in ratios:
            normalized_distribution[ratio] = ratio / total
        return normalized_distribution
if __name__ == '__main__':
    converter = WeightRatioConverter()
    sample_ratios = [10, 30, 60, 100]
    normalized_result = converter.convert_to_normalized_distribution(sample_ratios)
    print(normalized_result)