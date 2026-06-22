def max_in_sets(sets):
    return {key: max(value) for key, value in sets.items()}

if __name__ == '__main__':
    sample_sets = {
        'set1': [3, 5, 1],
        'set2': [8, 2, 9],
        'set3': [4, 7, 6]
    }
    print(max_in_sets(sample_sets))