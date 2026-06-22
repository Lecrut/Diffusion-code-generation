def calculate_weight_difference(weight1: float, weight2: float) -> float:
    def compute_absolute_difference(a: float, b: float) -> float:
        return abs(a - b)
    
    difference = compute_absolute_difference(weight1, weight2)
    return difference

if __name__ == '__main__':
    sample_weight_a = 60.8
    sample_weight_b = 55.3
    result = calculate_weight_difference(sample_weight_a, sample_weight_b)
    print(result)