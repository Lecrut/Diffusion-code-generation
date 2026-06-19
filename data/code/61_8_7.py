def retrieve_element(data_list, index):
    if 0 <= index < len(data_list):
        return data_list[index]
    else:
        raise IndexError("Index out of bounds")

if __name__ == '__main__':
    example_list = [15, 25, 35, 45, 55]
    desired_index = 1
    try:
        element = retrieve_element(example_list, desired_index)
        print(element)
    except IndexError as e:
        print(f"Error: {e}")