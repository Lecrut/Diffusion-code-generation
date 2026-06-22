import math

def _normalize_weight(value):
    if isinstance(value, int):
        return float(value)
    return float(value)

def calculate_weight_difference(weight1, weight2):
    n1 = _normalize_weight(weight1)
    n2 = _normalize_weight(weight2)
    if n1 >= n2:
        return n1 - n2
    return n2 - n1

class WeightComparator:
    def __init__(self, w1, w2):
        self.w1 = w1
        self.w2 = w2
    
    def get_difference(self):
        return calculate_weight_difference(self.w1, self.w2)

if __name__ == '__main__':
    sample_a = 250.75
    sample_b = 245.10
    direct_result = calculate_weight_difference(sample_a, sample_b)
    print(direct_result)
    comparator = WeightComparator(180.0, 200.5)
    print(comparator.get_difference())