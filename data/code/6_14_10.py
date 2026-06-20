def calculate_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    weight_a = 150
    weight_b = 120
    print(calculate_weight_difference(weight_a, weight_b))