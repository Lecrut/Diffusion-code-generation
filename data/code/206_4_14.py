def find_smallest(data):
    return min(data) if data else None

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, -5, 3]
    list3 = [42]
    list4 = []
    print(f"Smallest in {list1}: {find_smallest(list1)}")
    print(f"Smallest in {list2}: {find_smallest(list2)}")
    print(f"Smallest in {list3}: {find_smallest(list3)}")
    print(f"Smallest in {list4}: {find_smallest(list4)}")