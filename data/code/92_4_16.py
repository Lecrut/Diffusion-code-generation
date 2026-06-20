def get_opposite_boolean_string(bool_str):
    try:
        return 'False' if bool_str == 'True' else 'True'
    except TypeError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('False'))
    print(get_opposite_boolean_string(123))