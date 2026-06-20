def get_opposite_boolean_string(bool_str):
    bool_map = {'True': 'False', 'False': 'True'}
    return bool_map.get(bool_str, None)

if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))
    print(get_opposite_boolean_string('SomethingElse'))