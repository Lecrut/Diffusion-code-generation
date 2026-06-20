def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weight_a = 150.5
    weight_b = 132.2
    result = calculate_weight_difference(weight_a, weight_b)
    print(result)