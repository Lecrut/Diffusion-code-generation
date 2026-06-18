import sys
def find_max_value(numbers):
    if not numbers:
        return None
    max_val = -sys.maxsize
    for num in numbers:
        if isinstance(num, (int, float)) and num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    sample_list = [3, 5, 12, 89, -4]
    result = find_max_value(sample_list)
    print(result if result is not None else "No valid maximum found")