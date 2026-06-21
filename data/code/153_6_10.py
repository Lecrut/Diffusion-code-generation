def tuple_exists(target_tuple, list_of_tuples):
    return target_tuple in list_of_tuples

if __name__ == '__main__':
    sample_list = [(1, 2), (3, 4), (5, 6)]
    sample_tuple = (3, 4)
    print(tuple_exists(sample_tuple, sample_list))