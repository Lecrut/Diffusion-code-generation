class WeightRatioConverter:
    def convert_ratios_to_distribution(self, ratios):
        if not ratios:
            return {}
        total = sum(ratios)
        if total == 0:
            return {ratio: 0.0 for ratio in ratios}
        distribution = {}
        for ratio in ratios:
            distribution[ratio] = ratio / total
        return distribution
if __name__ == '__main__':
    converter = WeightRatioConverter()
    sample_ratios = [10, 30, 60, 100]
    normalized_distribution = converter.convert_ratios_to_distribution(sample_ratios)
    print(normalized_distribution)