def get_opposite_boolean_string(bool_str):
    if bool_str == 'True':
        return 'False'
    elif bool_str == 'False':
        return 'True'
    else:
        raise ValueError("Invalid boolean string")

if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))
    try:
        print(get_opposite_boolean_string('SomethingElse'))
    except ValueError as e:
        print(e)