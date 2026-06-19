def calculate_weight_difference(weight1, weight2):
    return abs(float(weight1) - float(weight2))

if __name__ == '__main__':
    weight_a = 75.5
    weight_b = 68.3
    difference = calculate_weight_difference(weight_a, weight_b)
    print(difference)