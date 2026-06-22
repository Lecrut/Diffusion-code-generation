def find_last_occurrence(lst, element):
    for index in range(len(lst) - 1, -1, -1):
        if lst[index] == element:
            return index
    return -1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6, 3]
    target_element = 3
    result = find_last_occurrence(sample_list, target_element)
    print(result)