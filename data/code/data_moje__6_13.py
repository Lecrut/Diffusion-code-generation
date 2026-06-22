def compute_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    w1 = 75.5
    w2 = 68.2
    result = compute_weight_difference(w1, w2)
    print(result)