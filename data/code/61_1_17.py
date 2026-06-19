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
    print(f"Sample List: {sample_list}")
    try:
        result1 = get_element_at_position(sample_list, 2)
        print(f"Element at index 2: {result1}")
        result2 = get_element_at_position(sample_list, 0)
        print(f"Element at index 0: {result2}")
        result3 = get_element_at_position(sample_list, 4)
        print(f"Element at index 4: {result3}")
    except IndexError as e:
        print(f"IndexError occurred: {e}")
    except TypeError as e:
        print(f"TypeError occurred: {e}")