def get_opposite_boolean_string(bool_str):
    if bool_str == 'True':
        return 'False'
    elif bool_str == 'False':
        return 'True'
    else:
        raise ValueError(f"Unsupported boolean string: {bool_str}")
if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))