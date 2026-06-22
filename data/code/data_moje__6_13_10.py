def get_weight_difference(weight_a: float, weight_b: float) -> float:
    return weight_a - weight_b

if __name__ == '__main__':
    hard_coded_weight_1 = 150.5
    hard_coded_weight_2 = 120.3
    result = get_weight_difference(hard_coded_weight_1, hard_coded_weight_2)
    print(result)