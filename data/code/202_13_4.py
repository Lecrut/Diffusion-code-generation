def calculate_max_value(numbers):
    if not numbers:
        raise ValueError("Input iterable cannot be empty")
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
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