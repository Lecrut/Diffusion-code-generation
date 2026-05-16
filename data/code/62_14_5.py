def get_second_element(data):
    if len(data) >= 2:
        return data[1]
    else:
        return None
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5]
    list3 = []
    list4 = [100]
    list5 = [1, 2]
    print(f"List {list1}: {get_second_element(list1)}")
    print(f"List {list2}: {get_second_element(list2)}")
    print(f"List {list3}: {get_second_element(list3)}")
    print(f"List {list4}: {get_second_element(list4)}")
    print(f"List {list5}: {get_second_element(list5)}")