weight_diff = lambda a, b: abs(a - b)

if __name__ == '__main__':
    weight_a = 100
    weight_b = 250
    result = weight_diff(weight_a, weight_b)
    print(result)