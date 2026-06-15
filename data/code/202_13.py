def calculate_max_value(numbers):
    if not numbers:
        raise ValueError("Input iterable cannot be empty")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    list1 = [3, 1, 9, 4, 7]
    print(f"Max of {list1}: {calculate_max_value(list1)}")
    tuple2 = (100, 50, 200, 10)
    print(f"Max of {tuple2}: {calculate_max_value(tuple2)}")
    list3 = [-5, -1, -10]
    print(f"Max of {list3}: {calculate_max_value(list3)}")
    empty_list = []
    try:
        calculate_max_value(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")