def find_max_value(numbers):
    if not numbers:
        return None
    max_val = float('-inf')
    for num in numbers:
        if isinstance(num, (int, float)):
            if num > max_val:
                max_val = num
    return int(max_val)
if __name__ == '__main__':
    sample_list = [34, 78, -12, 90, 56]
    result = find_max_value(sample_list)
    if result is not None:
        print(f"Maximum value in the list {sample_list} is: {result}")
    else:
        print("The input list was empty.")