def sort_two_floats(a, b):
    first = min(a, b)
    second = max(a, b)
    return first, second

if __name__ == '__main__':
    sample_a = 3.14
    sample_b = 2.71
    result = sort_two_floats(sample_a, sample_b)
    print(result)