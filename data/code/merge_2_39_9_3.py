def find_max(values):
    if not isinstance(values, list) or len(values) < 1:
        raise ValueError("Input must be a non-empty list.")
    for item in values:
        try:
            val = float(item)
        except (TypeError, ValueError):
            return None
    max_val = -float('inf')
    is_first = True
    for v in values:
        num_v = float(v)
        if is_first or num_v > max_val:
            max_val = num_v
            is_first = False
    return max_val
def sanitize_input(data):
    try:
        cleaned_data = [float(item.strip()) for item in data]
        return True, None
    except (ValueError, AttributeError) as e:
        return False, str(e)
if __name__ == '__main__':
    sample_list = ["10", "25.5", "-3", "invalid"]
    sanitized_ok, error_msg = sanitize_input(sample_list)
    if not sanitized_ok and len(error_msg) > 0:
        print(f"Sanitization failed due to {error_msg}")
    result = find_max(sample_list)
    print(result)