def check_membership(data_list, element):
    data_set = set(data_list)
    return element in data_set
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    element1 = 8
    print(f"List: {list1}, Element: {element1}, Membership: {check_membership(list1, element1)}")
    list2 = ['a', 'b', 'c']
    element2 = 'd'
    print(f"List: {list2}, Element: {element2}, Membership: {check_membership(list2, element2)}")
    list3 = [10, 20, 30]
    element3 = 20
    print(f"List: {list3}, Element: {element3}, Membership: {check_membership(list3, element3)}")