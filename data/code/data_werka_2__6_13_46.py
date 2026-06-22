def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weight_a = 50.9
    weight_b = 47.2
    difference = calculate_absolute_difference(weight_a, weight_b)
    print(difference)