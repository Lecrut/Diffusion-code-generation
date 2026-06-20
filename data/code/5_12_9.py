def compare_lengths_in_meters(m1, m2):
    cm1 = m1 * 100
    cm2 = m2 * 100
    if cm1 >= cm2:
        return m1, 'meters'
    else:
        return m2, 'meters'

if __name__ == '__main__':
    val, unit = compare_lengths_in_meters(5, 3)
    print(f"{val}{unit}")