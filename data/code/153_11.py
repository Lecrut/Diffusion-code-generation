import time
def item_exists(data, item):
    return item in data
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    item1 = 8
    result1 = item_exists(list1, item1)
    print(f"List: {list1}, Item: {item1}, Exists: {result1}")
    list2 = ['a', 'b', 'c', 'd']
    item2 = 'z'
    result2 = item_exists(list2, item2)
    print(f"List: {list2}, Item: {item2}, Exists: {result2}")
    list3 = [100, 200, 300]
    item3 = 200
    result3 = item_exists(list3, item3)
    print(f"List: {list3}, Item: {item3}, Exists: {result3}")
    list4 = []
    item4 = 5
    result4 = item_exists(list4, item4)
    print(f"List: {list4}, Item: {item4}, Exists: {result4}")