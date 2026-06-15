def calculate_max_value(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    max_val = data[0]
    for x in data[1:]:
        if x > max_val:
            max_val = x
    return max_val
if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"Max of {sample1}: {calculate_max_value(sample1)}")
    sample2 = [-10, -5, -20, -1]
    print(f"Max of {sample2}: {calculate_max_value(sample2)}")
    sample3 = [42]
    print(f"Max of {sample3}: {calculate_max_value(sample3)}")
    sample4 = [100, 50, 200, 10]
    print(f"Max of {sample4}: {calculate_max_value(sample4)}")
    try:
        calculate_max_value([])
    except ValueError as e:
        print(f"Error caught for empty list: {e}")