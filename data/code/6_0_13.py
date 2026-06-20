def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    w1 = 150.5
    w2 = 120.3
    diff = calculate_weight_difference(w1, w2)
    print(diff)