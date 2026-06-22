def calculate_absolute_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    weight_1 = 150.75
    weight_2 = 145.20
    result = calculate_absolute_difference(weight_1, weight_2)
    print(result)