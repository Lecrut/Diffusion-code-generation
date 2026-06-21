def find_last_occurrence(lst, element):
    reverse_index = -1
    for index in range(len(lst) - 1, -1, -1):
        if lst[index] == element:
            reverse_index = index
            break
    return reverse_index

if __name__ == '__main__':
    SAMPLE_LIST = [7, 5, 9, 3, 5, 2, 5]
    TARGET_ELEMENT = 5
    result = find_last_occurrence(SAMPLE_LIST, TARGET_ELEMENT)
    print(result)

    EMPTY_LIST = []
    NOT_FOUND_TARGET = 8
    empty_result = find_last_occurrence(EMPTY_LIST, NOT_FOUND_TARGET)
    print(empty_result)

    SINGLE_ELEMENT_LIST = [1]
    SINGLE_TARGET = 1
    single_result = find_last_occurrence(SINGLE_ELEMENT_LIST, SINGLE_TARGET)
    print(single_result)