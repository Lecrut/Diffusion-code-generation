def calculate_weight_difference(weight_a, weight_b):
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    w1 = 150.5
    w2 = 142.75
    print(calculate_weight_difference(w1, w2))