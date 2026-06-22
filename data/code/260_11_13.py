def find_max_in_sets(sets):
    if not all(isinstance(s, set) for s in sets.values()):
        raise ValueError("All values must be sets")
    
    max_values = {key: max(value) for key, value in sets.items()}
    return max_values

if __name__ == '__main__':
    sample_sets = {
        'set1': {1, 2, 3},
        'set2': {4, 5, 6},
        'set3': {7, 8, 9}
    }
    result = find_max_in_sets(sample_sets)
    print(result)