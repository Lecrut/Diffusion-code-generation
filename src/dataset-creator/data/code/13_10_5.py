def find_max_value(numbers):
    if not numbers:
        return None
    max_val = float('-inf')
    for num in numbers:
        try:
            val = int(num) if isinstance(num, str) else num
            if val > max_val:
                max_val = val
        except (ValueError, TypeError):
            continue
    return max_val
if __name__ == '__main__':
    sample_list = [34, 56, -20, '12', 89.5]
    result = find_max_value(sample_list)
    if result is not None:
        print(f"Maximum value found: {result}")
    else:
        print("No valid maximum value could be determined.")