def compute_weight_difference(weight_a: float, weight_b: float) -> float:
    return weight_a - weight_b

if __name__ == '__main__':
    sample_weight_a = 150.0
    sample_weight_b = 120.5
    result = compute_weight_difference(sample_weight_a, sample_weight_b)
    print(result)