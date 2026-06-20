def calculate_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    initial_weight = 150.5
    final_weight = 145.2
    difference = calculate_weight_difference(initial_weight, final_weight)
    print(difference)