def get_element(data, row_idx, col_idx, fallback=None):
    try:
        return data[row_idx][col_idx]
    except IndexError:
        return fallback

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    result_valid = get_element(sample_data, 1, 2)
    result_out_of_bounds = get_element(sample_data, 5, 1)
    result_negative = get_element(sample_data, -1, 0)
    
    print(result_valid)
    print(result_out_of_bounds)
    print(result_negative)