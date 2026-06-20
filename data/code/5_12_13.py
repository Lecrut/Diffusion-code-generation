def get_larger_value_in_original_unit(m1, m2):
    cm1 = m1 * 100
    cm2 = m2 * 100
    if cm1 > cm2:
        return m1
    else:
        return m2

if __name__ == '__main__':
    result = get_larger_value_in_original_unit(1.5, 2.0)
    print(result)