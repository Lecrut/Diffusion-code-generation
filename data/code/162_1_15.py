CONVERSION_DICT = {
    "color": 1,
    "size": 2,
    "details": 3,
    "status": 4
}

def map_to_integer_values(keys):
    return [CONVERSION_DICT.get(key, 0) for key in keys]

if __name__ == '__main__':
    sample_keys = ["color", "unknown_key", "size"]
    integer_values = map_to_integer_values(sample_keys)
    print(integer_values)