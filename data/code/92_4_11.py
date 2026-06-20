def get_opposite_boolean_string(bool_str):
    if bool_str == 'True':
        return 'False'
    elif bool_str == 'False':
        return 'True'
    else:
        raise ValueError("Invalid boolean string")

if __name__ == '__main__':
    sample_values = ['True', 'False', 'True']
    for value in sample_values:
        try:
            print(get_opposite_boolean_string(value))
        except ValueError as e:
            print(e)