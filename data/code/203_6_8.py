def find_first_mismatch_index(tuple1, tuple2):
    min_length = min(len(tuple1), len(tuple2))
    for index in range(min_length):
        if tuple1[index] != tuple2[index]:
            return index
    return -1
if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4)
    sample_tuple2 = (1, 2, 5, 4)
    result = find_first_mismatch_index(sample_tuple1, sample_tuple2)
    print(result)