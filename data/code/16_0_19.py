def _validate_non_empty_list(data):
    if not data:
        raise ValueError("List must not be empty")
    return True

def get_first_element(data):
    _validate_non_empty_list(data)
    return data[0]

if __name__ == '__main__':
    sample_list = [99, 88, 77]
    result = get_first_element(sample_list)
    print(result)