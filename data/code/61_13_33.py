def get_element_at_index(lst, index):
    return lst[index] if 0 <= index < len(lst) else None

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    indices_to_test = {
        'valid_index': 2,
        'out_of_bounds_high': 6,
        'negative_index': -1
    }
    
    for key, index in indices_to_test.items():
        result = get_element_at_index(sample_list, index)
        print(f"{key}: {result}")