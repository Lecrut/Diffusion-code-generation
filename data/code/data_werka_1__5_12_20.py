def convert_and_compare(meters1, meters2):
    cm1 = meters1 * 100
    cm2 = meters2 * 100
    if cm1 > cm2:
        return meters1
    else:
        return meters2

if __name__ == '__main__':
    value1 = 5.5
    value2 = 3.8
    result = convert_and_compare(value1, value2)
    print(result)