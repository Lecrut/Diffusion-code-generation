def calculate_absolute_difference(weight_one, weight_two):
    return abs(weight_one - weight_two)

if __name__ == '__main__':
    weight_a = 150.5
    weight_b = 120.75
    result = calculate_absolute_difference(weight_a, weight_b)
    print(result)