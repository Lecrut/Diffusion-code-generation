LOOKUP_TABLE_KEYS = ['apple', 'banana', 'cherry']
LOOKUP_TABLE_VALUES = [1, 2, 3]

def create_lookup_table(keys, values):
    return dict(zip(keys, values))

if __name__ == '__main__':
    lookup_table = create_lookup_table(LOOKUP_TABLE_KEYS, LOOKUP_TABLE_VALUES)
    print(lookup_table)