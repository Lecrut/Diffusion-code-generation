def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [3, 6, 9, 12, 15, 18]
    first_element, last_element = check_first_and_last(sample_list)
    print(f"First element: {first_element}")
    print(f"Last element: {last_element}")

    sample_list_single = [7]
    first_single, last_single = check_first_and_last(sample_list_single)
    print(f"First element (single element list): {first_single}")

    empty_list = []
    first_empty, last_empty = check_first_and_last(empty_list)
    print(f"First element (empty list): {first_empty}")
    print(f"Last element (empty list): {last_empty}")