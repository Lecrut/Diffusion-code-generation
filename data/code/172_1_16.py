def build_lookup_table(keys, values):
    return dict(zip(keys, values))

if __name__ == '__main__':
    sample_keys = ['cat', 'dog', 'bird']
    sample_values = [4, 4, 2]
    lookup_table = build_lookup_table(sample_keys, sample_values)
    print(lookup_table)