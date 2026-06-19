def convert_and_compare(meter1, meter2):
    cm1 = meter1 * 100
    cm2 = meter2 * 100
    if cm1 > cm2:
        return meter1
    else:
        return meter2

if __name__ == '__main__':
    value1 = 5.5
    value2 = 3.7
    result = convert_and_compare(value1, value2)
    print(result)