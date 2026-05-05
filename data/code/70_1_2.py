def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    first_element, last_element = check_first_and_last(sample_list)
    print(f"First element: {first_element}")
    print(f"Last element: {last_element}")
    sample_list_empty = []
    first_element_empty, last_element_empty = check_first_and_last(sample_list_empty)
    print(f"First element (empty list): {first_element_empty}")
    print(f"Last element (empty list): {last_element_empty}")
    sample_list_single = [99]
    first_element_single, last_element_single = check_first_and_last(sample_list_single)
    print(f"First element (single element list): {first_element_single}")
    print(f"Last element (single element list): {last_element_single}")