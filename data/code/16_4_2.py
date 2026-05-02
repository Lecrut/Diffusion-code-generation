def check_all_positive(numbers):
    return all(n > 0 for n in numbers)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, -2, 3]
    list3 = [0, 1, 3]
    list4 = []
    list5 = [5]
    print(f"List {list1}: {check_all_positive(list1)}")
    print(f"List {list2}: {check_all_positive(list2)}")
    print(f"List {list3}: {check_all_positive(list3)}")
    print(f"List {list4}: {check_all_positive(list4)}")
    print(f"List {list5}: {check_all_positive(list5)}")