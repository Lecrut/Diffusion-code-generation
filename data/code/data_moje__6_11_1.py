def calculate_absolute_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    first_weight = 123.456
    second_weight = 987.654
    result = calculate_absolute_difference(first_weight, second_weight)
    print(result)