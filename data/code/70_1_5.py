def check_first_and_last(data):
    if not data:
        return None, None
    first_element = data[0]
    last_element = data[-1]
    return first_element, last_element

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    first_val_1, last_val_1 = check_first_and_last(sample_list_1)
    print(f"First: {first_val_1}, Last: {last_val_1}")

    sample_list_2 = [7, 8, 9]
    first_val_2, last_val_2 = check_first_and_last(sample_list_2)
    print(f"First: {first_val_2}, Last: {last_val_2}")

    sample_list_empty = []
    first_val_empty, last_val_empty = check_first_and_last(sample_list_empty)
    print(f"First (empty list): {first_val_empty}, Last (empty list): {last_val_empty}")

    sample_list_single = [42]
    first_val_single, last_val_single = check_first_and_last(sample_list_single)
    print(f"First (single element list): {first_val_single}, Last (single element list): {last_val_single}")