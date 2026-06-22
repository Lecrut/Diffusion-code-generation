def find_max_in_sets(set_dict):
    max_values = {}
    for key, values in set_dict.items():
        max_values[key] = max(values)
    return max_values

if __name__ == '__main__':
    sample_sets = {
        'set1': [3, 5, 2, 8],
        'set2': [10, 4, 6, 7],
        'set3': [1, 9, 5, 3]
    }
    max_values = find_max_in_sets(sample_sets)
    print(max_values)