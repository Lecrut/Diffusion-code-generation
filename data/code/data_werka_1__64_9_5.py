def find_last_index(lst, target):
    last_index = -1
    for index, value in enumerate(lst):
        if value == target:
            last_index = index
    return last_index

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5, 2]
    target_value = 2
    result = find_last_index(sample_list, target_value)
    print(result)