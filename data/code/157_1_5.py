def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for item in data[1:]:
        if item < smallest:
            smallest = item
    return smallest
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 50, -5]
    empty_list = []
    list3 = [42]
    print(f"Smallest in {list1}: {find_smallest(list1)}")
    print(f"Smallest in {list2}: {find_smallest(list2)}")
    try:
        print(f"Smallest in {empty_list}: {find_smallest(empty_list)}")
    except ValueError as e:
        print(f"Error for {empty_list}: {e}")
    print(f"Smallest in {list3}: {find_smallest(list3)}")