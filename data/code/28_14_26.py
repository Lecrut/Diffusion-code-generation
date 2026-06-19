def compare_values(a, b):
    if not isinstance(a, float) or not isinstance(b, float):
        raise TypeError('Both inputs must be of type float')
    import math
    epsilon = 1e-09
    return a > b and (not math.isclose(a, b, rel_tol=epsilon))
if __name__ == '__main__':
    value1 = 3.141592653589793
    value2 = 3.141592653589793
    result = compare_values(value1, value2)
    print(result)