def compare_measurements(m1: float, m2: float) -> tuple:
    difference = m1 - m2
    ratio = m1 / m2 if m2 != 0 else float('inf')
    is_greater = m1 > m2
    return (difference, ratio, is_greater)

if __name__ == '__main__':
    length1 = 10.5
    length2 = 5.2
    result = compare_measurements(length1, length2)
    print(result)