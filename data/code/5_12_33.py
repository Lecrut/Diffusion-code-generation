def compare_lengths(meter1, meter2):
    cm1 = meter1 * 100
    cm2 = meter2 * 100
    if cm1 > cm2:
        return meter1
    else:
        return meter2

if __name__ == '__main__':
    length1 = 5.2
    length2 = 3.8
    larger_length = compare_lengths(length1, length2)
    print(larger_length)