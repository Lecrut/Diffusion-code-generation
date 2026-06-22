def find_extremes(nested_list):
    min_val = float('inf')
    max_val = float('-inf')
    for sublist in nested_list:
        for num in sublist:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_data = [[3, 5, 1], [2, 8], [7]]
    print(find_extremes(sample_data))