def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    first_weight = 85.75
    second_weight = 90.25
    difference = calculate_absolute_difference(first_weight, second_weight)
    print(difference)