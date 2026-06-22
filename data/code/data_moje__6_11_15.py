def calculate_absolute_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weight1 = 75.5
    weight2 = 82.3
    result = calculate_absolute_weight_difference(weight1, weight2)
    print(result)