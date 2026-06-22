def get_first_element(data):
    if not data:
        raise IndexError("list is empty")
    return data[0]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [1, 2, 3, 4]
    SAMPLE_LIST_2 = ['a', 'b', 'c']
    EMPTY_LIST = []

    try:
        first_element_1 = get_first_element(SAMPLE_LIST_1)
        print(f"First element of {SAMPLE_LIST_1}: {first_element_1}")
    except IndexError as e:
        print(f"Error caught for {SAMPLE_LIST_1}: {e}")

    try:
        first_element_2 = get_first_element(SAMPLE_LIST_2)
        print(f"First element of {SAMPLE_LIST_2}: {first_element_2}")
    except IndexError as e:
        print(f"Error caught for {SAMPLE_LIST_2}: {e}")

    try:
        get_first_element(EMPTY_LIST)
    except IndexError as e:
        print(f"Error caught for empty list: {e}")