BOOL_MAP = {'True': 'False', 'False': 'True'}

def flip_boolean_string(value: str) -> str:
    if value not in BOOL_MAP:
        raise ValueError(f"Invalid boolean string: {value}")
    return BOOL_MAP[value]

if __name__ == '__main__':
    print(flip_boolean_string('True'))
    print(flip_boolean_string('False'))
    print(flip_boolean_string('True'))
    print(flip_boolean_string('False'))