def find_max_in_sets(sets_dict):
    max_values = {}
    for key, values in sets_dict.items():
        max_value = max(values)
        max_values[key] = max_value
    return max_values

if __name__ == '__main__':
    sample_sets = {
        'Set 1': [3, 5, 1, 2],
        'Set 2': [7, 4, 6],
        'Set 3': [8, 0, -1]
    }
    result = find_max_in_sets(sample_sets)
    print(result)