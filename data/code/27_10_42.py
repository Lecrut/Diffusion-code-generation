def check_difference(value1, value2):
    tolerance = 1e-10
    return abs(value1 - value2) > tolerance

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = check_difference(value1, value2)
    print(result)