def calculate_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    input_weight_1 = 500
    input_weight_2 = 375
    result = calculate_weight_difference(input_weight_1, input_weight_2)
    print(result)