def find_first_mismatch(tup1, tup2):
    for index, (item1, item2) in enumerate(zip(tup1, tup2)):
        if item1 != item2:
            return index
    return -1
if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4)
    sample_tuple2 = (1, 2, 5, 4)
    print(find_first_mismatch(sample_tuple1, sample_tuple2))