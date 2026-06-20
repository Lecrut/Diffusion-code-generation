def filter_tuples(tuples, min_value, max_length):
    if not isinstance(min_value, (int, float)) or not isinstance(max_length, int) or max_length < 1:
        raise ValueError('Invalid input')
    return [t for t in tuples if min_value <= sum(t) <= max_value and len(t) == max_length]
if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]
    result = filter_tuples(sample_tuples, 10, 2)
    print(result)