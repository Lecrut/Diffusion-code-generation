def _validate_list(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) < 2:
        raise IndexError("List must contain at least two elements")

def get_second_last_element(data_list):
    _validate_list(data_list)
    return data_list[-2]

if __name__ == '__main__':
    sample_items = [100, 200, 300, 400, 500]
    output = get_second_last_element(sample_items)
    print(output)