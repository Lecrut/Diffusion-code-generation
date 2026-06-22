TOLERANCE = 1e-9

def is_significantly_different(a, b):
    return abs(a - b) > TOLERANCE

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = is_significantly_different(value1, value2)
    print(result)