def calculate_weight_difference(weight1, weight2):
    if weight1 > weight2:
        return weight1 - weight2
    return weight2 - weight1

if __name__ == '__main__':
    result = calculate_weight_difference(150.5, 120.75)
    print(result)
    result2 = calculate_weight_difference(45.0, 100.2)
    print(result2)