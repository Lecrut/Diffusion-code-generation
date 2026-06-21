class WeightDistributor:
    DEFAULT_TOTAL_WEIGHT = 100

    @staticmethod
    def calculate_total_ratio(weight_ratios):
        return sum(weight_ratios.values())

    @staticmethod
    def distribute_weight(weight_ratios, total_weight):
        if not weight_ratios:
            return {}
        
        total_ratio = WeightDistributor.calculate_total_ratio(weight_ratios)
        if total_ratio == 0:
            return {key: 0 for key in weight_ratios}
        
        distribution = {
            key: (value / total_ratio) * total_weight for key, value in weight_ratios.items()
        }
        return distribution

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    sample_total_weight = WeightDistributor.DEFAULT_TOTAL_WEIGHT
    result = WeightDistributor.distribute_weight(sample_ratios, sample_total_weight)
    print(result)