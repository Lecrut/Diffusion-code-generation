def compute_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    weight_a = 85.5
    weight_b = 70.3
    difference = compute_weight_difference(weight_a, weight_b)
    print(difference)