def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    indices_to_test = {
        'valid': 2,
        'out_of_bounds_high': 10,
        'out_of_bounds_low': -6
    }
    
    for key, idx in indices_to_test.items():
        result = get_element_at_index(sample_list, idx)
        print(f"Index {idx} ({key}): {result}")