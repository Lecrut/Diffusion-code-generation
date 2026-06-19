def convert_and_compare(m1, m2):
    cm1 = m1 * 100
    cm2 = m2 * 100
    if cm1 > cm2:
        return f"{m1} meters"
    else:
        return f"{m2} meters"

if __name__ == '__main__':
    length1 = 5.5
    length2 = 3.8
    print(convert_and_compare(length1, length2))