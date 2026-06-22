def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weight_a = 100.5
    weight_b = 85.2
    difference = calculate_weight_difference(weight_a, weight_b)
    print(difference)