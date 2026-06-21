def find_first_mismatch(tuple1, tuple2):
    length = min(len(tuple1), len(tuple2))
    for index in range(length):
        if tuple1[index] != tuple2[index]:
            return index
    return -1
if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4, 5)
    sample_tuple2 = (1, 2, 2, 4, 6)
    result = find_first_mismatch(sample_tuple1, sample_tuple2)
    print(result)