def compute_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    input_a = 42.5
    input_b = 18.3
    result = compute_weight_difference(input_a, input_b)
    print(result)