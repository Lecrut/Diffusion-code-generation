def check_item_exists(item, data_list):
    return item in data_list
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    item1 = 3
    print(f"List: {list1}, Item: {item1}, Exists: {check_item_exists(item1, list1)}")
    list2 = ['apple', 'banana', 'cherry']
    item2 = 'apple'
    print(f"List: {list2}, Item: {item2}, Exists: {check_item_exists(item2, list2)}")
    list3 = [True, False, True]
    item3 = False
    print(f"List: {list3}, Item: {item3}, Exists: {check_item_exists(item3, list3)}")
    list4 = [10, 20, 30]
    item4 = 5
    print(f"List: {list4}, Item: {item4}, Exists: {check_item_exists(item4, list4)}")
    list5 = []
    item5 = 1
    print(f"List: {list5}, Item: {item5}, Exists: {check_item_exists(item5, list5)}")
    list6 = ['a', 'b']
    item6 = 'c'
    print(f"List: {list6}, Item: {item6}, Exists: {check_item_exists(item6, list6)}")