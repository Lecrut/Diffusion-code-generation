def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest
if __name__ == '__main__':
    list1 = [5, 2, 8, -1, 0, -5]
    list2 = [-10, -5, -20, -1]
    list3 = [3, 3, 3, 3]
    list4 = [0, 0, 0, 0]
    list5 = [100]
    list6 = [-50]
    list7 = []
    print(f"Smallest in {list1}: {find_smallest(list1)}")
    print(f"Smallest in {list2}: {find_smallest(list2)}")
    print(f"Smallest in {list3}: {find_smallest(list3)}")
    print(f"Smallest in {list4}: {find_smallest(list4)}")
    print(f"Smallest in {list5}: {find_smallest(list5)}")
    print(f"Smallest in {list6}: {find_smallest(list6)}")
    try:
        find_smallest(list7)
    except ValueError as e:
        print(f"Error for {list7}: {e}")