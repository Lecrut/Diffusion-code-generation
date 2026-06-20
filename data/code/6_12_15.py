def compute_weight_difference(weight1: float, weight2: float) -> float:
    return weight2 - weight1

if __name__ == '__main__':
    sample_weight1 = 10.5
    sample_weight2 = 15.3
    result = compute_weight_difference(sample_weight1, sample_weight2)
    print(result)