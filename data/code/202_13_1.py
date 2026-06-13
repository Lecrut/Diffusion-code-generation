def calculate_max_value(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    max_val = data[0]
    for item in data[1:]:
        if item > max_val:
            max_val = item
    return max_val
if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"Max value of {sample1}: {calculate_max_value(sample1)}")
    sample2 = [-10, -5, -20, -1]
    print(f"Max value of {sample2}: {calculate_max_value(sample2)}")
    sample3 = [42]
    print(f"Max value of {sample3}: {calculate_max_value(sample3)}")
    sample4 = []
    try:
        calculate_max_value(sample4)
    except ValueError as e:
        print(f"Error for empty list: {e}")