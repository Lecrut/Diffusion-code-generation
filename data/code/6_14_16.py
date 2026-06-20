def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weight_a = 100.5
    weight_b = 45.3
    result = calculate_weight_difference(weight_a, weight_b)
    print(result)