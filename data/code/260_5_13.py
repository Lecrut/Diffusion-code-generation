def max_tuple_elements(tuple1, tuple2):
    return tuple((max(a, b) for a, b in zip(tuple1, tuple2)))
if __name__ == '__main__':
    sample_tuple1 = (1, 3, 5)
    sample_tuple2 = (2, 2, 6)
    result = max_tuple_elements(sample_tuple1, sample_tuple2)
    print(result)