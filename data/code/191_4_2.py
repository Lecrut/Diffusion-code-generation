def combine_tuples(tuple_list1, tuple_list2):
    combined = tuple_list1[:]
    combined.extend(tuple_list2)
    return combined

if __name__ == '__main__':
    sample_tuple1 = [(9, 10), (11, 12)]
    sample_tuple2 = [(13, 14), (15, 16)]
    result = combine_tuples(sample_tuple1, sample_tuple2)
    print(result)