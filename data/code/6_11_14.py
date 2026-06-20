def absolute_difference(w1, w2):
    return abs(w1 - w2)

if __name__ == '__main__':
    weight_a = 150.5
    weight_b = 120.25
    result = absolute_difference(weight_a, weight_b)
    print(result)