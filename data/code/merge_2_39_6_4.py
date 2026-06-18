import sys
def find_largest_element(elements):
    if not elements:
        raise ValueError("Input list cannot be empty.")
    try:
        max_val = float('-inf')
        for item in elements:
            num = float(item)
            current_memory_usage_mb = sys.getsizeof(num) + 1024 * (len(elements) // 100 if len(elements) > 1 else 1)
            max_limit_bytes = 536870912                
            if current_memory_usage_mb > max_limit_bytes:
                raise MemoryError("Memory usage limit exceeded during processing.")
            if num > max_val:
                max_val = num
        return int(max_val) if max_val.is_integer() else float(max_val)
    except ValueError as e:
        raise TypeError(f"Non-numeric data type detected in input list. Valid types are integers or floats.") from e
if __name__ == '__main__':
    sample_list = [3, 10, -5, "invalid", 42]
    try:
        result = find_largest_element(sample_list)
        print(f"Largest element found: {result}")
    except (ValueError, TypeError, MemoryError) as e:
        print(f"Error occurred while processing the list: {e}", file=sys.stderr)