from math import gcd

class WeightRatioConverter:
    @staticmethod
    def _validate_weights(weight1, weight2):
        if not isinstance(weight1, float) or not isinstance(weight2, float):
            raise ValueError("Both weights must be floats.")
        if weight1 <= 0 or weight2 <= 0:
            raise ValueError("Weights must be positive numbers.")

    @staticmethod
    def simplify(weight1, weight2):
        WeightRatioConverter._validate_weights(weight1, weight2)
        
        scaling_factor = 1000
        scaled_weight1 = int(weight1 * scaling_factor)
        scaled_weight2 = int(weight2 * scaling_factor)
        
        common_divisor = gcd(scaled_weight1, scaled_weight2)
        simplified_weight1 = scaled_weight1 // common_divisor
        simplified_weight2 = scaled_weight2 // common_divisor
        
        return (simplified_weight1, simplified_weight2)

if __name__ == '__main__':
    weight1 = 4.5
    weight2 = 2.25
    result = WeightRatioConverter.simplify(weight1, weight2)
    print(result)