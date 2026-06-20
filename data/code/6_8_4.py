def calculate_weight_difference(w1, w2):
    return abs(w1 - w2)

if __name__ == '__main__':
    w1 = 10.5
    w2 = 5.2
    result = calculate_weight_difference(w1, w2)
    print(result)