def find_last_index(lst, value):
    last_index = -1
    for i in range(len(lst)):
        if lst[i] == value:
            last_index = i
    return last_index

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5, 2]
    target_value = 2
    result = find_last_index(sample_list, target_value)
    print(result)