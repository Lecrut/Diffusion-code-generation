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
    list2 = [-10, -5, -20, -1]
    list3 = [0, 5, -3, 10]
    list4 = [-1, 0, 5, -100]
    list5 = [42]
    list6 = []
    print(f"Smallest in {list1}: {find_smallest(list1)}")
    print(f"Smallest in {list2}: {find_smallest(list2)}")
    print(f"Smallest in {list3}: {find_smallest(list3)}")
    print(f"Smallest in {list4}: {find_smallest(list4)}")
    print(f"Smallest in {list5}: {find_smallest(list5)}")
    try:
        find_smallest(list6)
    except ValueError as e:
        print(f"Error for {list6}: {e}")