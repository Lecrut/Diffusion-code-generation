def _validate_list(input_list):
    if not isinstance(input_list, (list, tuple)):
        raise TypeError("Expected a list or tuple")
    if len(input_list) < 3:
        raise ValueError("List must contain at least three elements")
    return True

def fetch_third_element(items):
    _validate_list(items)
    return items[2]

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400]
    value = fetch_third_element(sample_data)
    print(value)