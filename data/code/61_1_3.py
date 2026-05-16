def get_element_at_position(data_list, index):
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list.")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index < 0 or index >= len(data_list):
        raise IndexError("Index out of bounds.")
    return data_list[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Testing valid indices:")
    try:
        print(f"Element at index 0: {get_element_at_position(sample_list, 0)}")
        print(f"Element at index 2: {get_element_at_position(sample_list, 2)}")
        print(f"Element at index 4: {get_element_at_position(sample_list, 4)}")
    except Exception as e:
        print(f"An unexpected error occurred during valid tests: {e}")
    print("\nTesting invalid indices:")
    invalid_indices = [-1, 5, 10]
    for index in invalid_indices:
        try:
            print(f"Attempting to access index {index}: ", end="")
            get_element_at_position(sample_list, index)
        except IndexError as e:
            print(f"Caught expected error: {e}")
        except TypeError as e:
            print(f"Caught expected error: {e}")
        except Exception as e:
            print(f"Caught unexpected error: {e}")