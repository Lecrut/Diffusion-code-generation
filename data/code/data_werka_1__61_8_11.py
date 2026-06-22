def retrieve_element(data_list, index):
    if not isinstance(index, int) or index < 0:
        raise ValueError("Index must be a non-negative integer")
    try:
        return data_list[index]
    except IndexError:
        raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    target_index = 4
    try:
        element = retrieve_element(sample_data, target_index)
        print(element)
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")