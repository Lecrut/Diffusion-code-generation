import sys
def find_max_generator(iterable):
    if not iterable:
        return None
    max_val = float('-inf')
    for item in iterable:
        try:
            num = float(item)
            if num > max_val:
                max_val = num
        except (ValueError, TypeError):
            continue
    return max_val
if __name__ == '__main__':
    data = [10.5, "2", 3.7, None, -4, True, float('inf'), object()]
    result = find_max_generator(data)
    print(result if result is not None else "No valid maximum found")