def find_last_index(lst, target):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == target:
            return i
    return -1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 2, 1]
    target_value = 3
    result = find_last_index(sample_list, target_value)
    print(result)