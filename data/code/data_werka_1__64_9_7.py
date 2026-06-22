def find_last_index(lst, target):
    last_index = -1
    for index in range(len(lst)):
        if lst[index] == target:
            last_index = index
    return last_index

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 3, 5, 3]
    target_value = 3
    result = find_last_index(sample_list, target_value)
    print(result)