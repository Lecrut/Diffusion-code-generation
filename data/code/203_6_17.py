def compare_tuples(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have the same length")
    
    for index in range(len(tuple1)):
        if tuple1[index] != tuple2[index]:
            return index
    
    return -1

if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4)
    sample_tuple2 = (1, 2, 5, 4)
    result = compare_tuples(sample_tuple1, sample_tuple2)
    print(result)