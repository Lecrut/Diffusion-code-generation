EPSILON = 1e-10

def are_values_different(a, b):
    return abs(a - b) > EPSILON

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = are_values_different(value1, value2)
    print(result)