def get_element_by_position(data, index):
    if not (0 <= index < len(data)):
        raise IndexError("index out of range")
    return data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"List: {sample_list}")
    try:
        result1 = get_element_by_position(sample_list, 2)
        print(f"Element at index 2: {result1}")
        result2 = get_element_by_position(sample_list, 0)
        print(f"Element at index 0: {result2}")
        result3 = get_element_by_position(sample_list, 4)
        print(f"Element at index 4: {result3}")
        result_error = get_element_by_position(sample_list, 5)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    try:
        result_error_neg = get_element_by_position(sample_list, -1)
    except IndexError as e:
        print(f"Caught expected error: {e}")