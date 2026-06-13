def check_membership(data_list, element):
    data_set = set(data_list)
    return element in data_set
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    element1 = 3
    print(f"Checking for {element1} in {list1}: {check_membership(list1, element1)}")
    list2 = ['a', 'b', 'c', 'd']
    element2 = 'x'
    print(f"Checking for {element2} in {list2}: {check_membership(list2, element2)}")
    list3 = [10, 20, 30]
    element3 = 20
    print(f"Checking for {element3} in {list3}: {check_membership(list3, element3)}")