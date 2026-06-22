def calculate_absolute_difference(weight1, weight2):
    difference = abs(weight1 - weight2)
    return difference

if __name__ == '__main__':
    first_weight_value = 80.5
    second_weight_value = 76.8
    weight_difference = calculate_absolute_difference(first_weight_value, second_weight_value)
    print(weight_difference)