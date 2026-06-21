class WeightDistributor:
    def __init__(self, weight_ratios):
        self.weight_ratios = weight_ratios

    def calculate_distribution(self, total_weight):
        if not self.weight_ratios or total_weight <= 0:
            return {item: 0 for item in self.weight_ratios}
        
        total_ratio = sum(self.weight_ratios.values())
        if total_ratio == 0:
            return {item: 0 for item in self.weight_ratios}
        
        distribution = {}
        for item, ratio in self.weight_ratios.items():
            distribution[item] = (ratio / total_ratio) * total_weight
        return distribution

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    distributor = WeightDistributor(sample_ratios)
    
    sample_total_weight1 = 100
    result1 = distributor.calculate_distribution(sample_total_weight1)
    print(result1)
    
    sample_total_weight2 = 200
    result2 = distributor.calculate_distribution(sample_total_weight2)
    print(result2)