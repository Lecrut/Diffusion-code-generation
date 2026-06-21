def find_first_mismatch(tuple1, tuple2):
    if not (isinstance(tuple1, tuple) and isinstance(tuple2, tuple)):
        raise ValueError('Both inputs must be tuples.')
    max_length = max(len(tuple1), len(tuple2))
    for index in range(max_length):
        if index < len(tuple1) and index < len(tuple2):
            if tuple1[index] != tuple2[index]:
                return index
        elif index >= len(tuple1):
            return index
        else:
            return index
    return -1
if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4, 5)
    sample_tuple2 = (1, 2, 4, 4, 5)
    result = find_first_mismatch(sample_tuple1, sample_tuple2)
    print(result)