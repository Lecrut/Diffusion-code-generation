class WeightUtils:
    @staticmethod
    def abs_difference(a: float, b: float) -> float:
        return abs(a - b)

def calculate_weight_difference(weight1: float, weight2: float) -> float:
    return WeightUtils.abs_difference(weight1, weight2)

if __name__ == '__main__':
    sample_weight1 = 85.0
    sample_weight2 = 79.2
    difference = calculate_weight_difference(sample_weight1, sample_weight2)
    print(difference)