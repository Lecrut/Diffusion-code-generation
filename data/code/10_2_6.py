def _validate_input_sequence(data):
    return isinstance(data, tuple) and len(data) >= 1

def get_initial_element(source):
    if not _validate_input_sequence(source):
        return None
    return source[0]

if __name__ == '__main__':
    initial_data = (5, 15, 25, 35, 45)
    first_value = get_initial_element(initial_data)
    print(first_value)