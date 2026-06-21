KEYS = ['apple', 'banana', 'cherry']
VALUES = ['fruit', 'fruit', 'fruit']

def create_lookup_table(keys, values):
    return dict(zip(keys, values))

if __name__ == '__main__':
    lookup_table = create_lookup_table(KEYS, VALUES)
    print(lookup_table)