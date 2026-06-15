def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    list1 = [123456789, 987654321, 543210987]
    list2 = [-100, -50, -200, -1]
    list3 = [1, 2, 3, 4, 5]
    list4 = [999999999999999999999, 1234567890123456789]
    empty_list = []
    print(f"Largest in {list1}: {find_largest(list1)}")
    print(f"Largest in {list2}: {find_largest(list2)}")
    print(f"Largest in {list3}: {find_largest(list3)}")
    print(f"Largest in {list4}: {find_largest(list4)}")
    try:
        find_largest(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")