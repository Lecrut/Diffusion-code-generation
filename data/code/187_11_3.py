def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_largest(list1))
    list2 = [-10, -5, -20, -1]
    print(find_largest(list2))
    list3 = [42]
    print(find_largest(list3))
    list4 = [100]
    print(find_largest(list4))
    list5 = []
    try:
        print(find_largest(list5))
    except ValueError as e:
        print(f"Error: {e}")