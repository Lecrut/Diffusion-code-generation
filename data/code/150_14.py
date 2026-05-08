def remove_item(data_list, item_to_remove):
    try:
        data_list.remove(item_to_remove)
        return True
    except ValueError:
        return False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    item1 = 3
    success1 = remove_item(list1, item1)
    print(f"List: {list1}, Item: {item1}, Success: {success1}")
    list2 = [10, 20, 30]
    item2 = 99
    success2 = remove_item(list2, item2)
    print(f"List: {list2}, Item: {item2}, Success: {success2}")
    list3 = ['a', 'b', 'c']
    item3 = 'd'
    success3 = remove_item(list3, item3)
    print(f"List: {list3}, Item: {item3}, Success: {success3}")
    list4 = [5]
    item4 = 5
    success4 = remove_item(list4, item4)
    print(f"List: {list4}, Item: {item4}, Success: {success4}")