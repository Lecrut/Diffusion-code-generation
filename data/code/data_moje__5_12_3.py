def compare_lengths(m1, m2):
    cm1 = m1 * 100
    cm2 = m2 * 100
    if cm1 >= cm2:
        return m1
    return m2

if __name__ == '__main__':
    result = compare_lengths(5.0, 3.5)
    print(result)