def find_element_at_index(data_list, index):
    if 0 <= index < len(data_list):
        return data_list[index]
    else:
        raise IndexError("Index out of bounds")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_index = 2
    try:
        result = find_element_at_index(sample_list, target_index)
        print(result)
    except IndexError as e:
        print(f"Error: {e}")