def compare_meters(val1, val2):
    cm1 = val1 * 100
    cm2 = val2 * 100
    if cm1 > cm2:
        return val1
    elif cm2 > cm1:
        return val2
    else:
        return val1

if __name__ == '__main__':
    result = compare_meters(1.5, 2.0)
    print(result)
    result2 = compare_meters(3.0, 2.5)
    print(result2)
    result3 = compare_meters(1.0, 1.0)
    print(result3)