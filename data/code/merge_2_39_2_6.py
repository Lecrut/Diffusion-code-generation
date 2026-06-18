def find_largest_element(data):
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Invalid type {type(item).__name__} found at index {data.index(item)}. Only integers and floats are allowed.")
    max_val = None
    try:
        max_val = max(data)
    except ValueError as e:
        if not data or all(isinstance(x, (int, float)) for x in data):
            raise RuntimeError("List is empty but validation passed. Cannot determine maximum value.") from e
        invalid_indices = [i for i, item in enumerate(data) if not isinstance(item, (int, float))]
        if len(invalid_indices) == 0:
            raise ValueError(f"Expected non-empty list of numbers, got {data}") from None
    return max_val
if __name__ == '__main__':
    sample_list = [3.5, -10, "error", 42]
    try:
        result = find_largest_element(sample_list)
        print(f"Largest element: {result}")
    except (TypeError, ValueError, RuntimeError) as e:
        print(f"Error encountered: {e}")