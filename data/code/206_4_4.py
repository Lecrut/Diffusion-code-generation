def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 3, -5, 0, 7]
    list3 = [42]
    list4 = [100, 50, 25, 150]
    empty_list = []
    print(f"Smallest in {list1}: {find_smallest(list1)}")
    print(f"Smallest in {list2}: {find_smallest(list2)}")
    print(f"Smallest in {list3}: {find_smallest(list3)}")
    print(f"Smallest in {list4}: {find_smallest(list4)}")
    try:
        find_smallest(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")