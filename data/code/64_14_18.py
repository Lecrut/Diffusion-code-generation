def find_last_occurrence(lst, element):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == element:
            return i
    return -1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6, 3]
    element_to_find = 3
    index = find_last_occurrence(sample_list, element_to_find)
    print(index)