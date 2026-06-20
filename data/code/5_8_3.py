def compare_lengths(a, b):
    diff = abs(a - b)
    if a > b:
        desc = "First length is greater"
    elif b > a:
        desc = "Second length is greater"
    else:
        desc = "Lengths are equal"
    return (diff, desc)

if __name__ == '__main__':
    sample_a = 5.5
    sample_b = 3.2
    result = compare_lengths(sample_a, sample_b)
    print(result)

    sample_c = 10.0
    sample_d = 10.0
    result_equal = compare_lengths(sample_c, sample_d)
    print(result_equal)

    sample_e = 2.1
    sample_f = 7.8
    result_second = compare_lengths(sample_e, sample_f)
    print(result_second)