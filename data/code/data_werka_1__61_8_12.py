def fetch_element_by_index(data_sequence, target_position):
    try:
        return data_sequence[target_position]
    except IndexError:
        raise ValueError("Provided index is out of the sequence bounds")

if __name__ == '__main__':
    example_list = [100, 200, 300, 400, 500]
    desired_index = 3
    try:
        found_element = fetch_element_by_index(example_list, desired_index)
        print(found_element)
    except ValueError as error_message:
        print(f"Error: {error_message}")