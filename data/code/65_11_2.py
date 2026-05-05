def get_element_by_position(data, index):
    if not (0 <= index < len(data)):
        raise IndexError("index out of range")
    return data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_element_by_position(sample_list, 2))
    try:
        get_element_by_position(sample_list, 5)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    try:
        get_element_by_position(sample_list, -1)
    except IndexError as e:
        print(f"Caught expected error: {e}")