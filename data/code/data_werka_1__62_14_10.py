class SafeListAccess:
    def __init__(self, data):
        self.data = data

    def get_second_element(self):
        if len(self.data) >= 2:
            return self.data[1]
        else:
            return None

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5]
    list3 = []
    list4 = [100]

    safe_list1 = SafeListAccess(list1)
    safe_list2 = SafeListAccess(list2)
    safe_list3 = SafeListAccess(list3)
    safe_list4 = SafeListAccess(list4)

    print(f"List {list1}: {safe_list1.get_second_element()}")
    print(f"List {list2}: {safe_list2.get_second_element()}")
    print(f"List {list3}: {safe_list3.get_second_element()}")
    print(f"List {list4}: {safe_list4.get_second_element()}")