from math import gcd

class WeightRatioConverter:
    @staticmethod
    def simplify(weight1, weight2):
        if not (isinstance(weight1, float) and isinstance(weight2, float)):
            raise ValueError("Both inputs must be floats.")
        
        scale_factor = 1000
        scaled_weight1 = int(weight1 * scale_factor)
        scaled_weight2 = int(weight2 * scale_factor)
        
        common_divisor = gcd(scaled_weight1, scaled_weight2)
        simplified_weight1 = scaled_weight1 // common_divisor
        simplified_weight2 = scaled_weight2 // common_divisor
        
        return (simplified_weight1, simplified_weight2)

if __name__ == '__main__':
    sample_weight1 = 4.5
    sample_weight2 = 2.25
    try:
        result = WeightRatioConverter.simplify(sample_weight1, sample_weight2)
        print(result)
    except ValueError as e:
        print(e)