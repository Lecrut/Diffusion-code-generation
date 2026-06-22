def compare_lengths(a: float, b: float) -> tuple:
    if a > b:
        return (a, b, "greater")
    elif a < b:
        return (a, b, "less")
    else:
        return (a, b, "equal")

if __name__ == '__main__':
    sample_a = 3.14
    sample_b = 2.71
    result = compare_lengths(sample_a, sample_b)
    print(result)

    sample_c = 5.0
    sample_d = 5.0
    result_equal = compare_lengths(sample_c, sample_d)
    print(result_equal)

    sample_e = 1.5
    sample_f = 2.5
    result_less = compare_lengths(sample_e, sample_f)
    print(result_less)