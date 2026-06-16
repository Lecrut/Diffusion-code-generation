def find_max(numbers):
    if not numbers:
        return None
    max_val = float('-inf')
    for num in numbers:
        try:
            val = int(num)
            if val > max_val:
                max_val = val
        except ValueError:
            continue
    return max_val
if __name__ == '__main__':
    sample_list = [3, 50, -12, 'invalid', 7]
    result = find_max(sample_list)
    print(result if result is not None else "Empty list")