def max_values_tuples(tuple1, tuple2):
    if not (isinstance(tuple1, tuple) and isinstance(tuple2, tuple)):
        raise ValueError('Both inputs must be tuples.')
    if len(tuple1) != len(tuple2):
        raise ValueError('Tuples must have the same length.')
    return tuple((max(value1, value2) for value1, value2 in zip(tuple1, tuple2)))
if __name__ == '__main__':
    sample_tuple1 = (5, 3, 9, 1)
    sample_tuple2 = (2, 8, 4, 7)
    result = max_values_tuples(sample_tuple1, sample_tuple2)
    print(result)