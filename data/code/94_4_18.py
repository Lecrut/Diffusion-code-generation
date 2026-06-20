def check_existence(data_list):
    if not isinstance(data_list, list) or not all(isinstance(item, bool) for item in data_list):
        raise ValueError("Input must be a list of boolean values")
    
    return any(data_list)

if __name__ == '__main__':
    list1 = [False, False, False]
    list2 = [False, True, False]
    list3 = []
    list4 = [True, True]
    list5 = [False]
    print(f"list1: {check_existence(list1)}")
    print(f"list2: {check_existence(list2)}")
    print(f"list3: {check_existence(list3)}")
    print(f"list4: {check_existence(list4)}")
    print(f"list5: {check_existence(list5)}")