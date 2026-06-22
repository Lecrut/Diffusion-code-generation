def calculate_weight_difference(weight_one, weight_two):
    return abs(weight_one - weight_two)

if __name__ == '__main__':
    weight_a = 150.5
    weight_b = 120.3
    difference = calculate_weight_difference(weight_a, weight_b)
    print(difference)