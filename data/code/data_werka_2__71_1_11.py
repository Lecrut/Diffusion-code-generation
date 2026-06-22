def find_middle_element(lst):
    LOWER_INDEX_OFFSET = 1
    ELEMENTS_COUNT = len(lst)
    if ELEMENTS_COUNT == 0:
        raise ValueError("List cannot be empty")
    middle_index = (ELEMENTS_COUNT - LOWER_INDEX_OFFSET) // 2
    return lst[middle_index]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [100, 200, 300, 400]
    single_list = [999]
    print(find_middle_element(odd_list))
    print(find_middle_element(even_list))
    print(find_middle_element(single_list))