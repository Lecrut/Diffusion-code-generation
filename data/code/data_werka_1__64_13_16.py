def find_final_index(indices):
    NO_INDEX_FOUND = -1
    if not indices:
        return NO_INDEX_FOUND
    return max(indices)

if __name__ == '__main__':
    SAMPLE_LIST_1 = [1, 5, 3, 8, 2]
    SAMPLE_LIST_2 = [10, 20, 5]
    SINGLE_ELEMENT_LIST = [42]
    EMPTY_LIST = []

    print(find_final_index(SAMPLE_LIST_1))
    print(find_final_index(SAMPLE_LIST_2))
    print(find_final_index(SINGLE_ELEMENT_LIST))
    print(find_final_index(EMPTY_LIST))