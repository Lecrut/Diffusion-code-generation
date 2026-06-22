def max_values_tuple(tuple1, tuple2):
    return tuple((max(value1, value2) for value1, value2 in zip(tuple1, tuple2)))
if __name__ == '__main__':
    sample_tuple1 = (3, 5, 7)
    sample_tuple2 = (2, 6, 4)
    result = max_values_tuple(sample_tuple1, sample_tuple2)
    print(result)