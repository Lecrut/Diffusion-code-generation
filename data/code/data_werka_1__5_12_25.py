def compare_lengths(meter1, meter2):
    cm1 = meter1 * 100
    cm2 = meter2 * 100
    if cm1 > cm2:
        return f"{meter1} meters"
    else:
        return f"{meter2} meters"

if __name__ == '__main__':
    length1 = 5.5
    length2 = 3.7
    result = compare_lengths(length1, length2)
    print(result)