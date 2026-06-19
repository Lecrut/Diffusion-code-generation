def are_values_differently_typed(a, b):
    return type(a) != type(b)

def are_values_significantly_different(a, b, tolerance=1e-10):
    if are_values_differently_typed(a, b):
        return True
    return abs(a - b) > tolerance

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = are_values_significantly_different(value1, value2)
    print(result)