def calculate_weight_difference(weight1, weight2):
    return abs(float(weight1) - float(weight2))

if __name__ == '__main__':
    w1 = 150.5
    w2 = 175.2
    print(calculate_weight_difference(w1, w2))