def calculate_weight_difference(weight_a, weight_b):
    if weight_a < weight_b:
        return weight_b - weight_a
    return weight_a - weight_b

if __name__ == '__main__':
    weight1 = 150.5
    weight2 = 120.75
    result = calculate_weight_difference(weight1, weight2)
    print(result)