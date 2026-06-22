def find_extremes(nested_list):
    min_val = float('inf')
    max_val = float('-inf')
    for sublist in nested_list:
        for value in sublist:
            if value < min_val:
                min_val = value
            if value > max_val:
                max_val = value
    return min_val, max_val

if __name__ == '__main__':
    sample_data = [[3, 5, 1], [2, 8], [7, -1]]
    print(find_extremes(sample_data))