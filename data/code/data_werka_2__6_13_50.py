def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    initial_weight = 85.0
    compared_weight = 92.4
    absolute_diff = calculate_absolute_difference(initial_weight, compared_weight)
    print(absolute_diff)