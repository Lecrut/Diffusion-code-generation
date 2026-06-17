def find_max_float(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    list1 = [3.14159, 2.71828, 1.61803]
    list2 = [-5.0, -10.5, -2.2]
    list3 = [1.0, 1.0000000000000001, 1.0000000000000002]
    list4 = []
    print(f"Max in {list1}: {find_max_float(list1)}")
    print(f"Max in {list2}: {find_max_float(list2)}")
    print(f"Max in {list3}: {find_max_float(list3)}")
    try:
        find_max_float(list4)
    except ValueError as e:
        print(f"Error for empty list: {e}")