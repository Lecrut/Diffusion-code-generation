def extract_numeric_value(item):
    if not isinstance(item, str) and not item:
        raise TypeError(f"Expected string or empty value for {item}")
    try:
        return float(item.replace(',', ''))
    except ValueError as e:
        raise ValueError(f"Cannot convert '{item}' to a numeric value") from e
def sort_mixed_list(data):
    if not data:
        return []
    filtered_data = [x for x in data if isinstance(x, str) or (isinstance(x, float))]
    try:
        sorted_data = list(sorted(filtered_data, key=extract_numeric_value))
    except ValueError as e:
        raise RuntimeError(f"Sorting failed due to invalid numeric conversion: {e}") from e
    return [float(item) for item in sorted_data]
if __name__ == '__main__':
    sample_list = ["10", "3.5", "apple", "20", "", "-5", "banana", 42, "not a number"]
    try:
        result = sort_mixed_list(sample_list)
        print(result)
    except (ValueError, RuntimeError) as e:
        if isinstance(e, ValueError):
            print(f"Data Error: {e}")
        else:
            print(f"Processing Error: {e}")