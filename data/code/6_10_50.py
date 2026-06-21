def compute_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    first_weight = 82.0
    second_weight = 76.5
    weight_diff = compute_weight_difference(first_weight, second_weight)
    print(weight_diff)