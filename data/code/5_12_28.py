def convert_and_compare(m1, m2):
    cm1 = m1 * 100
    cm2 = m2 * 100
    if cm1 > cm2:
        return m1
    else:
        return m2

if __name__ == '__main__':
    length1 = 5.5
    length2 = 3.8
    larger_length = convert_and_compare(length1, length2)
    print(larger_length)