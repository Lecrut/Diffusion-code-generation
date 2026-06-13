def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_smallest(list1))
    list2 = [-10, 0, 5, -20, 3]
    print(find_smallest(list2))
    list3 = [42]
    print(find_smallest(list3))
    list4 = [7]
    print(find_smallest(list4))
    list5 = []
    try:
        print(find_smallest(list5))
    except ValueError as e:
        print(e)