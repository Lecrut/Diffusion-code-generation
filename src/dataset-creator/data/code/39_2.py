class InvalidTypeException(Exception):
    pass
def find_largest_element(data_list):
    if not data_list:
        raise ValueError("List is empty")
    valid_types = (int, float)
    for item in data_list:
        if not isinstance(item, valid_types):
            raise InvalidTypeException(f"Invalid type '{type(item).__name__}' found at index {data_list.index(item)}")
    return max(data_list)
if __name__ == '__main__':
    sample_data = [10, 25.5, "invalid", -3]
    try:
        result = find_largest_element(sample_data)
        print(f"Largest element: {result}")
    except InvalidTypeException as e:
        print(f"Error: {e}")