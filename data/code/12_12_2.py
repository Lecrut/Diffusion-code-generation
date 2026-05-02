class WeightRatioConverter:
    def convert_ratios_to_distribution(self, ratios):
        if not ratios:
            return None
        total = sum(ratios)
        if total == 0:
            return [0.0] * len(ratios)
        distribution = [ratio / total for ratio in ratios]
        return distribution
if __name__ == '__main__':
    converter = WeightRatioConverter()
    sample_ratios_1 = [10, 30, 60]
    distribution_1 = converter.convert_ratios_to_distribution(sample_ratios_1)
    print(f"Ratios: {sample_ratios_1}")
    print(f"Distribution: {distribution_1}")
    sample_ratios_2 = [1, 1, 1, 1]
    distribution_2 = converter.convert_ratios_to_distribution(sample_ratios_2)
    print(f"Ratios: {sample_ratios_2}")
    print(f"Distribution: {distribution_2}")
    sample_ratios_3 = [5, 5, 10]
    distribution_3 = converter.convert_ratios_to_distribution(sample_ratios_3)
    print(f"Ratios: {sample_ratios_3}")
    print(f"Distribution: {distribution_3}")
    sample_ratios_4 = [0, 0, 0]
    distribution_4 = converter.convert_ratios_to_distribution(sample_ratios_4)
    print(f"Ratios: {sample_ratios_4}")
    print(f"Distribution: {distribution_4}")