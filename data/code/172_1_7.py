def build_lookup_table(keys, values):
    return dict(zip(keys, values))

if __name__ == '__main__':
    KEY_LIST = ['apple', 'banana', 'cherry']
    VALUE_LIST = [10, 20, 30]
    LOOKUP_TABLE = build_lookup_table(KEY_LIST, VALUE_LIST)
    print(LOOKUP_TABLE)