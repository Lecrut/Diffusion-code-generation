def fetch_element_by_index(data_sequence, position):
    if 0 <= position < len(data_sequence):
        return data_sequence[position]
    else:
        raise IndexError("Index out of bounds")

if __name__ == '__main__':
    example_list = [7, 17, 27, 37, 47]
    desired_index = 1
    try:
        element_value = fetch_element_by_index(example_list, desired_index)
        print(element_value)
    except IndexError as e:
        print(f"Error: {e}")