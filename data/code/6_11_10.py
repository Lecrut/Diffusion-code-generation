def calculate_absolute_difference(weight1, weight2):
    return abs(weight1 - weight2)

if __name__ == '__main__':
    w1 = 72.5
    w2 = 68.3
    result = calculate_absolute_difference(w1, w2)
    print(result)