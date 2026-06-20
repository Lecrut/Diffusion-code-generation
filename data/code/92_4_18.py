def is_valid_boolean_string(bool_str):
    return bool_str in ('True', 'False')

def get_opposite_boolean_string(bool_str):
    if not is_valid_boolean_string(bool_str):
        raise ValueError("Invalid boolean string")
    return 'False' if bool_str == 'True' else 'True'

if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))