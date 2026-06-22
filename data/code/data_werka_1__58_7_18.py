def get_first_element(data):
    if not data:
        return None
    return data[0]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [1, 2, 3, 4]
    SAMPLE_LIST_2 = ['x', 'y', 'z']
    EMPTY_LIST = []
    SINGLE_ITEM_LIST = [999]

    print(f"First element of {SAMPLE_LIST_1}: {get_first_element(SAMPLE_LIST_1)}")
    print(f"First element of {SAMPLE_LIST_2}: {get_first_element(SAMPLE_LIST_2)}")
    print(f"First element of {EMPTY_LIST}: {get_first_element(EMPTY_LIST)}")
    print(f"First element of {SINGLE_ITEM_LIST}: {get_first_element(SINGLE_ITEM_LIST)}")