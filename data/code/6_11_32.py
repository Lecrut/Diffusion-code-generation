def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weight_a = 85.75
    weight_b = 90.30
    difference = calculate_absolute_difference(weight_a, weight_b)
    print(difference)