def is_greater(a, b):
    return a > b
if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    result = is_greater(sample_a, sample_b)
    print(result)
    sample_c = 3.5
    sample_d = 3.5
    result = is_greater(sample_c, sample_d)
    print(result)
    sample_e = 'apple'
    sample_f = 'banana'
    result = is_greater(sample_e, sample_f)
    print(result)
    sample_g = [1, 2, 3]
    sample_h = [1, 2]
    result = is_greater(sample_g, sample_h)
    print(result)