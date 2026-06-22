def find_the_middle_value_among_three_rank_samples(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    sample_values = (5, 7, 3)
    middle_value = find_the_middle_value_among_three_rank_samples(*sample_values)
    print(middle_value)