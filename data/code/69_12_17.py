def get_element(data_list, index):
    if not isinstance(data_list, list) or not all(isinstance(item, int) for item in data_list):
        raise TypeError("First argument must be a list of integers")
    
    if not isinstance(index, (int,)):
        raise ValueError("Second argument must be an integer")
    
    if not (-len(data_list) <= index < len(data_list)):
        raise IndexError("Index out of bounds")
    
    return data_list[index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        element_positive = get_element(sample_data, 2)
        print(f"Element at positive index 2: {element_positive}")
        element_negative = get_element(sample_data, -1)
        print(f"Element at negative index -1: {element_negative}")
        element_out_of_bounds = get_element(sample_data, 5)
    except IndexError as e:
        print(f"Caught expected error for out of bounds index: {e}")
    except ValueError as e:
        print(f"Caught expected error for invalid value: {e}")
    except TypeError as e:
        print(f"Caught expected error for invalid type: {e}")