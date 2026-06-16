def find_max(lst):
    if not lst:
        return None
    max_val = float('-inf')
    for item in lst:
        try:
            num = float(item)
            if num > max_val:
                max_val = num
        except (ValueError, TypeError):
            continue
    return int(max_val)
if __name__ == '__main__':
    sample_list = [3.5, 7, '10', -2, None]
    result = find_max(sample_list)
    print(result if result is not None else "Empty or invalid list")