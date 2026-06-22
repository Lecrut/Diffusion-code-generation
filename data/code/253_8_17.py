def find_the_middle_value_among_three_compare(a, b):
    return sorted([a, b])[1]

if __name__ == '__main__':
    sample_a = 9
    sample_b = 4
    result = find_the_middle_value_among_three_compare(sample_a, sample_b)
    print(result)