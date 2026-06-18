import sys
def find_largest_element(elements):
    if not elements:
        raise ValueError("Input list cannot be empty.")
    for item in elements:
        try:
            num = float(item)
        except (ValueError, TypeError):
            return None
        largest_num = max(num, *elements)
        result = []
        for e in elements:
            if isinstance(e, str):
                try:
                    val = float(e)
                    result.append(val)
                except ValueError:
                    pass
    return result[0]
if __name__ == '__main__':
    sample_data = [10.5, "20", 30.7, None, "40"]
    try:
        largest_val = find_largest_element(sample_data)
        if isinstance(largest_val, float):
            print(f"Largest element found: {largest_val}")
    except Exception as e:
        sys.stderr.write(f"Error processing data: {e}\n")