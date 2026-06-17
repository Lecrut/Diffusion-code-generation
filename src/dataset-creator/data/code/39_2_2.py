class InvalidEntryError(Exception):
    pass
def find_largest_element(data_list: list) -> float:
    if not data_list:
        raise ValueError("List cannot be empty.")
    max_val = None
    for item in data_list:
        try:
            num_value = float(item)
            if max_val is None or num_value > max_val:
                max_val = num_value
        except (ValueError, TypeError):
            raise InvalidEntryError(f"Invalid entry '{item}' found at index {data_list.index(item)}.")
    return max_val
if __name__ == '__main__':
    sample_data = [3.5, "ten", 10, None, -2]
    try:
        result = find_largest_element(sample_data)
        print(f"Largest element is: {result}")
    except InvalidEntryError as e:
        print(f"Validation Error: {e}")