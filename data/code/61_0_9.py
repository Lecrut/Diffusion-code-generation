def get_element_safely(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return "Index out of bounds"

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    indices_to_test = {
        'valid': 2,
        'invalid': 5
    }
    
    for key, index in indices_to_test.items():
        result = get_element_safely(sample_data, index)
        print(f"List: {sample_data}")
        print(f"Attempting to access {key} index {index}: {result}")