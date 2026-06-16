def find_largest_number(numbers):
    if not numbers:
        return None
    for item in numbers:
        try:
            num = float(item)
        except (ValueError, TypeError):
            raise ValueError(f"Non-numeric element found: {item}")
    max_val = -float('inf')
    for n in numbers:
        if isinstance(n, str):
            continue
        val = float(n)
        if val > max_val:
            max_val = val
    return int(max_val)
if __name__ == '__main__':
    sample_array = [3.5, 7, "10", -2, None]
    try:
        result = find_largest_number(sample_array)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")