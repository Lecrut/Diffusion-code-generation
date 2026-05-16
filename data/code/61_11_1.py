class InvalidIndexError(ValueError):
    pass
def get_element_at_position(data, index):
    if not isinstance(index, int):
        raise InvalidIndexError("Index must be an integer")
    if index < 0 or index >= len(data):
        raise InvalidIndexError(f"Index {index} is out of bounds for list of length {len(data)}")
    return data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"List: {sample_list}")
    try:
        result1 = get_element_at_position(sample_list, 2)
        print(f"Element at index 2: {result1}")
        result2 = get_element_at_position(sample_list, 0)
        print(f"Element at index 0: {result2}")
        result3 = get_element_at_position(sample_list, 4)
        print(f"Element at index 4: {result3}")
        print("-" * 20)
        get_element_at_position(sample_list, 5)
    except InvalidIndexError as e:
        print(f"Caught expected error: {e}")
    except ValueError as e:
        print(f"Caught unexpected ValueError: {e}")