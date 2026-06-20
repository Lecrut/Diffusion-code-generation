def negate_boolean(boolean_list):
    if not isinstance(boolean_list, list) or len(boolean_list) != 1:
        raise ValueError("Input must be a list containing exactly one boolean value.")
    return not boolean_list[0]

if __name__ == '__main__':
    sample_value = [True]
    try:
        print(negate_boolean(sample_value))
    except ValueError as e:
        print(e)