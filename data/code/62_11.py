def get_second_item(data):
    if len(data) > 1:
        return data[1]
    else:
        return None
if __name__ == '__main__':
    list1 = [10, 20, 30]
    list2 = [5]
    list3 = []
    list4 = [1]
    print(f"List {list1}: {get_second_item(list1)}")
    print(f"List {list2}: {get_second_item(list2)}")
    print(f"List {list3}: {get_second_item(list3)}")
    print(f"List {list4}: {get_second_item(list4)}")