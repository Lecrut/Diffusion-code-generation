def analyze_list_parity(data):
    all_even = True
    all_odd = True
    if not data:
        return True, True
    for x in data:
        if x % 2 != 0:
            all_even = False
        if x % 2 == 0:
            all_odd = False
    return all_even, all_odd
if __name__ == '__main__':
    list1 = [2, 4, 6, 8]
    list2 = [1, 3, 5, 7]
    list3 = [2, 4, 5, 6]
    list4 = []
    list5 = [1, 3]
    list6 = [2, 2]
    list7 = [1, 1]
    print(f"List {list1}: {analyze_list_parity(list1)}")
    print(f"List {list2}: {analyze_list_parity(list2)}")
    print(f"List {list3}: {analyze_list_parity(list3)}")
    print(f"List {list4}: {analyze_list_parity(list4)}")
    print(f"List {list5}: {analyze_list_parity(list5)}")
    print(f"List {list6}: {analyze_list_parity(list6)}")
    print(f"List {list7}: {analyze_list_parity(list7)}")