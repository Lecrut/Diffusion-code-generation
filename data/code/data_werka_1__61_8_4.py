def find_element_at_index(data_list, index):
    if not (0 <= index < len(data_list)):
        raise IndexError("Index out of bounds")
    return data_list[index]

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    target_index = 1
    try:
        result = find_element_at_index(sample_list, target_index)
        print(result)
    except IndexError as e:
        print(f"Error: {e}")