def find_first_mismatch(tup1, tup2):
    if not isinstance(tup1, tuple) or not isinstance(tup2, tuple):
        raise ValueError("Both inputs must be tuples.")
    
    min_length = min(len(tup1), len(tup2))
    for i in range(min_length):
        if tup1[i] != tup2[i]:
            return i
    return -1

if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4)
    sample_tuple2 = (1, 2, 5, 4)
    result = find_first_mismatch(sample_tuple1, sample_tuple2)
    print(result)