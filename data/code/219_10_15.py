def find_max(data):
    return max(data) if data else None

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -20, -1]
    list3 = [7]
    list4 = []
    print(f"Max of {list1}: {find_max(list1)}")
    print(f"Max of {list2}: {find_max(list2)}")
    print(f"Max of {list3}: {find_max(list3)}")
    print(f"Max of {list4}: {find_max(list4)}")