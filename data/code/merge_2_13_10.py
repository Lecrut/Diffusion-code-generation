def find_max(numbers):
    if not numbers:
        return None
    max_value = float('-inf')
    for num in numbers:
        if isinstance(num, (int, float)):
            if num > max_value:
                max_value = num
    return int(max_value)
if __name__ == '__main__':
    sample_list = [34, 78, -12, 90, 56]
    result = find_max(sample_list)
    if result is not None:
        print(f"Maximum value in the list: {result}")
    else:
        print("The input list was empty.")