def compute_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    val1 = 100.5
    val2 = 87.3
    result = compute_weight_difference(val1, val2)
    print(result)