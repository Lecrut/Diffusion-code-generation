def check_existence(data_list):
    if not data_list:
        return False
    return any(data_list)
if __name__ == '__main__':
    list1 = [False, False, False]
    list2 = [False, True, False]
    list3 = []
    list4 = [True, True, True]
    list5 = []
    list6 = [False]
    print(f"list1: {check_existence(list1)}")
    print(f"list2: {check_existence(list2)}")
    print(f"list3: {check_existence(list3)}")
    print(f"list4: {check_existence(list4)}")
    print(f"list5: {check_existence(list5)}")
    print(f"list6: {check_existence(list6)}")