def larger_in_original_unit(value1, value2):
    cm1 = value1 * 100
    cm2 = value2 * 100
    if cm1 >= cm2:
        return value1
    else:
        return value2

if __name__ == '__main__':
    result = larger_in_original_unit(1.5, 2.3)
    print(result)