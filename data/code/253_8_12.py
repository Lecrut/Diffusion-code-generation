def find_the_middle_value_among_three_compare(a, b):
    return sorted([a, b])[1]

if __name__ == '__main__':
    sample_a = 5
    sample_b = 3
    middle_value = find_the_middle_value_among_three_compare(sample_a, sample_b)
    print(middle_value)