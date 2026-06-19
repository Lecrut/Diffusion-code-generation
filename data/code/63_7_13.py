def find_first_element_o1(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [10, 20, 30, 40, 50]
    SAMPLE_LIST_2 = [99, 1, 5, 1000]
    SAMPLE_LIST_3 = [42]
    EMPTY_LIST = []

    try:
        print(f"First element of {SAMPLE_LIST_1}: {find_first_element_o1(SAMPLE_LIST_1)}")
        print(f"First element of {SAMPLE_LIST_2}: {find_first_element_o1(SAMPLE_LIST_2)}")
        print(f"First element of {SAMPLE_LIST_3}: {find_first_element_o1(SAMPLE_LIST_3)}")
    except IndexError as e:
        print(f"Error for non-empty lists: {e}")

    try:
        find_first_element_o1(EMPTY_LIST)
    except IndexError as e:
        print(f"List 4 (empty): {EMPTY_LIST}, Error: {e}")