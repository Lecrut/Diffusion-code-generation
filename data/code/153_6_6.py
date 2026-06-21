def tuple_exists(target_tuple, tuple_list):
    return target_tuple in tuple_list

if __name__ == '__main__':
    sample_tuple = (1, 2)
    sample_list = [(3, 4), (5, 6), (1, 2)]
    print(tuple_exists(sample_tuple, sample_list))