def remove_integer(lst, target):
    index_map = {value: idx for idx, value in enumerate(lst)}
    if target in index_map:
        lst.pop(index_map[target])

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    integer_to_remove = 30
    remove_integer(sample_list, integer_to_remove)
    print(sample_list)