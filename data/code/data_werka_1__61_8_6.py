MAX_INDEX = 1000

def retrieve_element(data_list, index):
    if 0 <= index < len(data_list) and index <= MAX_INDEX:
        return data_list[index]
    else:
        raise IndexError("Index out of bounds or exceeds maximum allowed index")

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    target_index = 7
    try:
        result = retrieve_element(sample_data, target_index)
        print(result)
    except IndexError as e:
        print(f"Error: {e}")