def extend_list(base_list, add_list):
    base_list.extend(add_list)
    return base_list

if __name__ == '__main__':
    sample_base = [1, 2, 3]
    sample_add = [4, 5, 6]
    result = extend_list(sample_base, sample_add)
    print(result)