def find_max_in_sets(sets):
    if not all((isinstance(s, set) for s in sets.values())):
        raise ValueError('All values must be sets')
    return {key: max(value) for key, value in sets.items()}
if __name__ == '__main__':
    sample_sets = {'set1': {1, 2, 3}, 'set2': {4, 5, 6}, 'set3': {7, 8, 9}}
    results = find_max_in_sets(sample_sets)
    print(results)