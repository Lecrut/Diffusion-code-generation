def compare_floats(a, b):
    tolerance = 1e-09
    if abs(a - b) < tolerance:
        return (a, 'equal')
    elif a > b:
        return (a, 'greater')
    else:
        return (b, 'greater')
if __name__ == '__main__':
    result1 = compare_floats(10.0000000001, 9.9999999999)
    print(result1)
    result2 = compare_floats(3.5, 4.5)
    print(result2)
    result3 = compare_floats(-2.5, -3.5)
    print(result3)
    result4 = compare_floats(0.0, 0.0)
    print(result4)