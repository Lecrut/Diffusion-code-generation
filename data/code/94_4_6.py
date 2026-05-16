def check_existence(data_list):
    if not data_list:
        return False
    for item in data_list:
        if item:
            return True
    return False
if __name__ == '__main__':
    list1 = [False, False, False]
    list2 = [False, True, False]
    list3 = []
    list4 = [True]
    list5 = []
    print(f"list1: {check_existence(list1)}")
    print(f"list2: {check_existence(list2)}")
    print(f"list3: {check_existence(list3)}")
    print(f"list4: {check_existence(list4)}")
    print(f"list5: {check_existence(list5)}")