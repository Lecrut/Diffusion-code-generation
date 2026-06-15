def calculate_max_value(numbers):
    if not numbers:
        raise ValueError("Input iterable cannot be empty")
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    sample1 = [3, 1, 9, 4, 7]
    print(f"Max of {sample1}: {calculate_max_value(sample1)}")
    sample2 = [-5, -10, -1, -8]
    print(f"Max of {sample2}: {calculate_max_value(sample2)}")
    sample3 = [42]
    print(f"Max of {sample3}: {calculate_max_value(sample3)}")
    sample4 = [100, 50, 200, 10]
    print(f"Max of {sample4}: {calculate_max_value(sample4)}")
    try:
        calculate_max_value([])
    except ValueError as e:
        print(f"Error caught for empty list: {e}")