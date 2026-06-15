def calculate_max_value(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    max_val = data[0]
    for x in data[1:]:
        if x > max_val:
            max_val = x
    return max_val
if __name__ == '__main__':
    sample1 = [3, 1, 9, 4, 7]
    sample2 = [-5, -10, -2, -8]
    sample3 = [42]
    sample4 = []
    print(f"Max of {sample1}: {calculate_max_value(sample1)}")
    print(f"Max of {sample2}: {calculate_max_value(sample2)}")
    print(f"Max of {sample3}: {calculate_max_value(sample3)}")
    try:
        calculate_max_value(sample4)
    except ValueError as e:
        print(f"Error for {sample4}: {e}")