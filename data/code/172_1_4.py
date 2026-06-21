def build_lookup_table(keys, values):
    lookup = {}
    for key, value in zip(keys, values):
        lookup[key] = value
    return lookup

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    sample_values = [1, 2, 3]
    table = build_lookup_table(sample_keys, sample_values)
    print(table)