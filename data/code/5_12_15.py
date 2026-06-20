def compare_lengths_in_cm(length1, length2):
    cm1 = length1 * 100
    cm2 = length2 * 100
    if cm1 >= cm2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    val1 = 1.5
    val2 = 2.0
    result = compare_lengths_in_cm(val1, val2)
    print(result)