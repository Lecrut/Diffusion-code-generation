def calculate_absolute_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    weight_one = 45.75
    weight_two = 120.30
    result = calculate_absolute_difference(weight_one, weight_two)
    print(result)