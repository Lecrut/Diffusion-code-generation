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
    list2 = [-10, 5, 0, -3, 12]
    list3 = [42]
    list4 = [7]
    list5 = []
    
    try:
        print(f"Smallest in {list1}: {find_smallest(list1)}")
        print(f"Smallest in {list2}: {find_smallest(list2)}")
        print(f"Smallest in {list3}: {find_smallest(list3)}")
        print(f"Smallest in {list4}: {find_smallest(list4)}")
    except ValueError as e:
        print(e)