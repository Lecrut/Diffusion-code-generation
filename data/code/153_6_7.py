def tuple_exists(target_tuple, tuple_list):
    return target_tuple in tuple_list

if __name__ == '__main__':
    sample_tuple = (3, 4)
    sample_list = [(1, 2), (3, 4), (5, 6)]
    print(tuple_exists(sample_tuple, sample_list))