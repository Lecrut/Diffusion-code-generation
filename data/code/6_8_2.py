def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    val1 = 150.5
    val2 = 120.3
    result = calculate_weight_difference(val1, val2)
    print(result)