def create_lookup_table(keys, values):
    return dict(zip(keys, values))

if __name__ == '__main__':
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    lookup_table = create_lookup_table(keys, values)
    print(lookup_table)