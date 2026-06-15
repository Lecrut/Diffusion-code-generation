def check_membership(data_list, item):
    return item in data_list
if __name__ == '__main__':
    list1 = [1, 5, 8, 10, 2]
    item1 = 8
    print(f"List: {list1}, Item: {item1}")
    print(f"Using 'in' operator: {check_membership(list1, item1)}")
    list2 = ['a', 'b', 'c', 'd']
    item2 = 'c'
    print(f"\nList: {list2}, Item: {item2}")
    print(f"Using 'in' operator: {check_membership(list2, item2)}")
    list3 = [100, 200, 300]
    item3 = 50
    print(f"\nList: {list3}, Item: {item3}")
    print(f"Using 'in' operator: {check_membership(list3, item3)}")
    large_list = list(range(10000))
    large_item_present = 5000
    large_item_absent = 10001
    print(f"\nLarge List check (Item present): {check_membership(large_list, large_item_present)}")
    print(f"Large List check (Item absent): {check_membership(large_list, large_item_absent)}")