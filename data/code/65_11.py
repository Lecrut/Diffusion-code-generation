def get_element_by_position(data, index):
    if not (0 <= index < len(data)):
        raise IndexError("index out of range")
    return data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        result1 = get_element_by_position(sample_list, 2)
        print(f"Element at index 2: {result1}")
        result2 = get_element_by_position(sample_list, 0)
        print(f"Element at index 0: {result2}")
        result3 = get_element_by_position(sample_list, 4)
        print(f"Element at index 4: {result3}")
        try:
            result4 = get_element_by_position(sample_list, 5)
            print(f"Element at index 5: {result4}")
        except IndexError as e:
            print(f"Caught expected error for index 5: {e}")
    except IndexError as e:
        print(f"An unexpected IndexError occurred: {e}")