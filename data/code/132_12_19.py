BOOLEAN_VALUES = {'true', 'false', '1', '0'}

def is_valid_boolean(value):
    normalized_value = value.lower()
    return normalized_value in BOOLEAN_VALUES
if __name__ == '__main__':
    print(is_valid_boolean('True'))
    print(is_valid_boolean('false'))
    print(is_valid_boolean('1'))
    print(is_valid_boolean('0'))
    print(is_valid_boolean('yes'))
    print(is_valid_boolean('no'))