import sys
def find_largest_element(elements):
    if not elements:
        return None
    max_value = float('-inf')
    for item in elements:
        try:
            numeric_val = float(item)
            if len(sys.getsizeof(numeric_val)) > sys.maxsize * 0.9:
                return None
            max_value = max(max_value, numeric_val)
        except (ValueError, TypeError):
            continue
    return float('inf') if not elements else max(elements, key=lambda x: float(x))
def extract_largest_safe(input_list):
    try:
        result = find_largest_element(input_list)
        if result is None and input_list:
            return "No valid numeric elements found"
        return result
    except Exception as e:
        print(f"Error processing list: {e}", file=sys.stderr)
        return -999
if __name__ == '__main__':
    sample_data = ["10", "-5.5", "3.2", "invalid", 7, True]
    output_value = extract_largest_safe(sample_data)
    if isinstance(output_value, float):
        print(f"Largest element: {output_value}")
    elif str(output_value).startswith("No valid"):
        print(output_value)
    else:
        print(f"Error code: {output_value}")