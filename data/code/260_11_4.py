def find_max_in_sets(sets_dict):
    return {key: max(value) for key, value in sets_dict.items()}

if __name__ == '__main__':
    sample_data = {
        'set1': [3, 5, 1, 2],
        'set2': [7, 8, 6, 9],
        'set3': [4, 0, -1, 10]
    }
    result = find_max_in_sets(sample_data)
    print(result)