def find_the_middle_value_among_three_filter_valid(sample):
    if len(sample) != 3:
        return None
    a, b, c = sample
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        return None
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_filter_valid([3, 1, 2]))
    print(find_the_middle_value_among_three_filter_valid([5.5, 4.4, 6.6]))
    print(find_the_middle_value_among_three_filter_valid(['a', 'b', 'c']))
    print(find_the_middle_value_among_three_filter_valid([1, 2]))