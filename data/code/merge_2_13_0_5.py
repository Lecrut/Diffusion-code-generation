def find_max(numbers):
    if not numbers:
        return None
    max_val = float('-inf')
    for num in numbers:
        try:
            val = float(num)
            if val > max_val:
                max_val = val
        except (ValueError, TypeError):
            continue
    return int(max_val)
if __name__ == '__main__':
    sample_list = [10, 25.3, None, 'a', -5]
    result = find_max(sample_list)
    print(result if result is not None else "Empty or invalid list")