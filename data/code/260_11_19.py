def find_max_in_sets(sets_dict):
    return {key: max(value) for key, value in sets_dict.items()}

if __name__ == '__main__':
    sample_data = {
        'set1': [3, 5, 1],
        'set2': [8, 2, 9],
        'set3': [4, 7, 6]
    }
    print(find_max_in_sets(sample_data))