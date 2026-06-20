def get_opposite_boolean_string(bool_str):
    return 'False' if bool_str == 'True' else ('True' if bool_str == 'False' else None)

if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))
    print(get_opposite_boolean_string('SomethingElse'))