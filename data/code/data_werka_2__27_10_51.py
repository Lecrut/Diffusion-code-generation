def is_significantly_different(a, b):
    epsilon = 1e-10
    return abs(a - b) > epsilon

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = is_significantly_different(value1, value2)
    print(result)