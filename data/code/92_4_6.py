def is_valid_boolean_string(bool_str):
    return bool_str in ('True', 'False')

def get_opposite_boolean_string(bool_str):
    if not is_valid_boolean_string(bool_str):
        raise ValueError("Invalid boolean string")
    
    return 'True' if bool_str == 'False' else 'False'

if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))
    try:
        print(get_opposite_boolean_string('SomethingElse'))
    except ValueError as e:
        print(e)