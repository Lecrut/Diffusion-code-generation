def is_valid_boolean(value):
    normalized_value = value.lower()
    return normalized_value in {'true', 'false', '1', '0'}

if __name__ == '__main__':
    test_values = ['True', 'false', '1', '0', 'yes', 'no']
    for val in test_values:
        print(f"'{val}': {is_valid_boolean(val)}")