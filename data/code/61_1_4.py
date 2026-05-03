def get_element_at_position(data, index):
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index < 0 or index >= len(data):
        raise IndexError("Index out of bounds.")
    return data[index]
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
            print(f"Attempting index {index}: ", end="")
            get_element_at_position(sample_list, index)
        except IndexError as e:
            print(f"Caught expected error: {e}")
        except Exception as e:
            print(f"Caught unexpected error: {e}")
    print("\nTesting invalid input types:")
    try:
        get_element_at_position("not a list", 1)
    except TypeError as e:
        print(f"Caught expected error for list type: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")
    try:
        get_element_at_position(sample_list, 1.5)
    except TypeError as e:
        print(f"Caught expected error for index type: {e}")
    except Exception as e:
        print(f"Caught unexpected error: {e}")