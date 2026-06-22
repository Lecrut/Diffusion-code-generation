def calculate_weight_difference(a, b):
    return abs(a - b)

if __name__ == '__main__':
    weight1 = 75.5
    weight2 = 68.3
    difference = calculate_weight_difference(weight1, weight2)
    print(difference)