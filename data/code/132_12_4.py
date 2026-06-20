def is_valid_boolean(value):
    boolean_mapping = {'true': True, 'false': False, '1': True, '0': False}
    normalized_value = value.lower()
    return normalized_value in boolean_mapping
if __name__ == '__main__':
    print(is_valid_boolean('True'))
    print(is_valid_boolean('false'))
    print(is_valid_boolean('1'))
    print(is_valid_boolean('0'))
    print(is_valid_boolean('yes'))
    print(is_valid_boolean('no'))