def get_opposite_boolean_string(bool_string):
    lower_string = bool_string.lower()
    if lower_string == 'true':
        return 'False'
    elif lower_string == 'false':
        return 'True'
    else:
        raise ValueError("Invalid boolean string provided")
if __name__ == '__main__':
    print(get_opposite_boolean_string('True'))
    print(get_opposite_boolean_string('false'))
    print(get_opposite_boolean_string('TRUE'))
    print(get_opposite_boolean_string('fAlSe'))
    try:
        get_opposite_boolean_string('Maybe')
    except ValueError as e:
        print(f"Error caught: {e}")