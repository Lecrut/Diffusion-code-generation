MAX_INDEX = 100

def retrieve_element(data_list, index):
    if not (0 <= index < len(data_list)):
        raise IndexError("Index out of bounds")
    return data_list[index]

if __name__ == '__main__':
    example_list = [5, 15, 25, 35, 45]
    desired_index = 2
    try:
        element = retrieve_element(example_list, desired_index)
        print(element)
    except IndexError as e:
        print(f"Error: {e}")