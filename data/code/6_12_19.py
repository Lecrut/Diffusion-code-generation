def compute_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    initial_weight = 150
    final_weight = 142
    result = compute_weight_difference(initial_weight, final_weight)
    print(result)