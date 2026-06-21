def build_lookup_table(keys, values):
    lookup = {}
    for key, value in zip(keys, values):
        lookup[key] = value
    return lookup

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    sample_values = [10, 20, 30]
    result_table = build_lookup_table(sample_keys, sample_values)
    print(result_table)