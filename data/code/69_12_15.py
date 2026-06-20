def get_element(data_list, index):
    if not (-len(data_list) <= index < len(data_list)):
        raise IndexError("Index out of bounds")
    return data_list[index]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    try:
        element1 = get_element(my_list, 2)
        print(f"Element at index 2: {element1}")
        element_out_of_bounds = get_element(my_list, 5)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    try:
        element_negative = get_element(my_list, -1)
        print(f"Element at negative index -1: {element_negative}")
    except IndexError as e:
        print(f"Caught expected error for negative index: {e}")