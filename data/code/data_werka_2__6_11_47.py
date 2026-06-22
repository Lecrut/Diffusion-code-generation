def compute_weight_difference(w1, w2):
    return abs(w1 - w2)

if __name__ == '__main__':
    weight_a = 70.0
    weight_b = 65.0
    difference = compute_weight_difference(weight_a, weight_b)
    print(difference)