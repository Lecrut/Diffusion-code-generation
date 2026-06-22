def calculate_weight_difference(num1, num2):
    return abs(num1 - num2)

if __name__ == '__main__':
    weight1 = 75.5
    weight2 = 68.2
    difference = calculate_weight_difference(weight1, weight2)
    print(difference)