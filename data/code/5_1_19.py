def compare_lengths(a: float, b: float) -> tuple:
    if a > b:
        return ('a', 'greater')
    elif a < b:
        return ('b', 'greater')
    else:
        return ('equal', 'equal')

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 7.2
    result = compare_lengths(sample_a, sample_b)
    print(result)
    sample_c = 3.0
    sample_d = 3.0
    result2 = compare_lengths(sample_c, sample_d)
    print(result2)
    sample_e = 1.1
    sample_f = 2.2
    result3 = compare_lengths(sample_e, sample_f)
    print(result3)