class WeightRatioConverter:
    def convert_ratios(self, ratios):
        if not ratios:
            return None
        total = sum(ratios)
        if total == 0:
            return [0.0] * len(ratios)
        normalized_distribution = [ratio / total for ratio in ratios]
        return normalized_distribution
if __name__ == '__main__':
    converter = WeightRatioConverter()
    sample_ratios_1 = [10, 30, 60]
    normalized_1 = converter.convert_ratios(sample_ratios_1)
    print(f"Sample Ratios 1: {sample_ratios_1}")
    print(f"Normalized Distribution 1: {normalized_1}")
    sample_ratios_2 = [1, 1, 1, 1]
    normalized_2 = converter.convert_ratios(sample_ratios_2)
    print(f"Sample Ratios 2: {sample_ratios_2}")
    print(f"Normalized Distribution 2: {normalized_2}")
    sample_ratios_3 = [5, 5, 10]
    normalized_3 = converter.convert_ratios(sample_ratios_3)
    print(f"Sample Ratios 3: {sample_ratios_3}")
    print(f"Normalized Distribution 3: {normalized_3}")
    sample_ratios_4 = [0, 0, 0]
    normalized_4 = converter.convert_ratios(sample_ratios_4)
    print(f"Sample Ratios 4: {sample_ratios_4}")
    print(f"Normalized Distribution 4: {normalized_4}")