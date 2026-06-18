def find_max(numbers):
    if not numbers:
        return None
    max_val = float('-inf')
    for num in numbers:
        try:
            n = int(num)
            if n > max_val:
                max_val = n
        except (ValueError, TypeError):
            continue
    return max_val
if __name__ == '__main__':
    sample_list = [10, 25.3, 'a', -5, None]
    result = find_max(sample_list)
    print(result if result is not None else "Empty or invalid list")