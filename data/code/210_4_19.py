def find_range(data):
    return min(data), max(data) if data else None

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = []
    list3 = [10]
    list4 = [-5, 0, 5]
    print(f"Range of {list1}: {find_range(list1)}")
    print(f"Range of {list2}: {find_range(list2)}")
    print(f"Range of {list3}: {find_range(list3)}")
    print(f"Range of {list4}: {find_range(list4)}")