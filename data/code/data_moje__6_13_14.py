def calculate_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    value_one = 150.5
    value_two = 120.75
    result = calculate_weight_difference(value_one, value_two)
    print(result)