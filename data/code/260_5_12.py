def max_values_in_tuples(tuple1, tuple2):
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise ValueError('Both arguments must be tuples')
    if len(tuple1) != len(tuple2):
        raise ValueError('Tuples must have the same length')
    return tuple((max(x, y) for x, y in zip(tuple1, tuple2)))
if __name__ == '__main__':
    sample_tuple1 = (3, 5, 7)
    sample_tuple2 = (2, 6, 4)
    result = max_values_in_tuples(sample_tuple1, sample_tuple2)
    print(result)