def tuple_exists(tuples_list, target_tuple):
    return target_tuple in tuples_list

if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 4), (5, 6)]
    target = (3, 4)
    print(tuple_exists(sample_tuples, target))