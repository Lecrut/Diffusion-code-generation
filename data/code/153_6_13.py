def tuple_exists(target_tuple, tuple_list):
    return target_tuple in tuple_list

if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 4), (5, 6)]
    target = (3, 4)
    result = tuple_exists(target, sample_tuples)
    print(f"Tuple {target} exists: {result}")