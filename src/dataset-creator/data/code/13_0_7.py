def find_max(numbers):
    if not numbers:
        return None
    max_val = float('-inf')
    for num in numbers:
        try:
            numeric_value = float(num)
            if numeric_value > max_val:
                max_val = numeric_value
        except (ValueError, TypeError):
            continue
    return int(max_val)
if __name__ == '__main__':
    sample_list = [3, 50, -12, 'invalid', 7.8]
    result = find_max(sample_list)
    print(result if result is not None else "Empty list")