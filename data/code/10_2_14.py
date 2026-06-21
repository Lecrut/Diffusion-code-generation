FIRST_VALUE_KEY = 'first'
TUPLE_MAPPING = {
    FIRST_VALUE_KEY: (100, 200, 300, 400, 500)
}

def get_tuple_from_key(key):
    return TUPLE_MAPPING[key]

def extract_first_index(tuple_data):
    return tuple_data[0]

def compute_first_value(key):
    data = get_tuple_from_key(key)
    return extract_first_index(data)

if __name__ == '__main__':
    print(compute_first_value(FIRST_VALUE_KEY))