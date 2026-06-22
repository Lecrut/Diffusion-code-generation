def find_max_min_difference(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    max_value = max(flat_list)
    min_value = min(flat_list)
    return max_value - min_value
if __name__ == '__main__':
    sample_nested_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    result = find_max_min_difference(sample_nested_list)
    print(result)