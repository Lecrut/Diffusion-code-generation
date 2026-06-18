def sort_mixed_list(data):
    if not data:
        return []
    try:
        numeric_data = [float(x) for x in data]
    except ValueError as e:
        raise TypeError(f"List contains non-numeric elements that cannot be converted to float. Error details: {e}")
    sorted_indices = list(range(len(numeric_data)))
    original_values = []
    try:
        numeric_only_list = [float(x) for x in data if isinstance(float(str(x)), (int, float))]
        full_conversion_error = None
        def validate_and_convert(item):
            try:
                return float(str(item))
            except ValueError as e:
                raise TypeError(f"Cannot convert element '{item}' to a number. Error details: {e}")
        numeric_values = []
        for item in data:
            if not isinstance(item, (int, float)):
                try:
                    val = validate_and_convert(item)
                    numeric_values.append(val)
                except TypeError as e:
                    raise ValueError(f"Invalid element '{item}' found at an expected position. Cannot sort mixed types without handling all elements.") from e
        sorted_indices.sort(key=lambda i: float(data[i]))
    except Exception as e:
        raise RuntimeError("Failed to process numeric values for sorting") from e
    return [data[sorted_index] for sorted_index in sorted_indices]
if __name__ == '__main__':
    sample_data = ["10", "2.5", "three", 4, "-7"]
    try:
        result = sort_mixed_list(sample_data)
        print("Sorted list:", result)
    except (TypeError, ValueError, RuntimeError) as e:
        print(f"Error during sorting: {e}")