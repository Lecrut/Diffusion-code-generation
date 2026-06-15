def find_max(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    data1 = [3.14, 1.618, 2.718, 0.577]
    data2 = [-10.5, -5.2, -20.1, -1.9]
    data3 = [42.0, 100.5, 33.3, 99.9]
    empty_data = []
    print(f"Max of {data1}: {find_max(data1)}")
    print(f"Max of {data2}: {find_max(data2)}")
    print(f"Max of {data3}: {find_max(data3)}")
    try:
        find_max(empty_data)
    except ValueError as e:
        print(f"Error for empty list: {e}")