def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, 0, 5, -20, 3]
    list3 = [7]
    empty_list = []
    print(f"Smallest in {list1}: {find_smallest(list1)}")
    print(f"Smallest in {list2}: {find_smallest(list2)}")
    print(f"Smallest in {list3}: {find_smallest(list3)}")
    try:
        find_smallest(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")