def get_opposite_boolean_string(bool_str):
    bool_str = bool_str.strip()
    if bool_str.lower() == 'true':
        return 'False'
    elif bool_str.lower() == 'false':
        return 'True'
    else:
        raise ValueError("Invalid boolean string provided")
if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))
    print(get_opposite_boolean_string('true'))
    print(get_opposite_boolean_string(' fAlSe '))
    try:
        print(get_opposite_boolean_string('Maybe'))
    except ValueError as e:
        print(e)