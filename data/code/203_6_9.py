def find_first_mismatch(tuple1, tuple2):
    for index, (item1, item2) in enumerate(zip(tuple1, tuple2)):
        if item1 != item2:
            return index
    return -1
if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4)
    sample_tuple2 = (1, 2, 5, 4)
    result = find_first_mismatch(sample_tuple1, sample_tuple2)
    print(result)