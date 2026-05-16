import time
def item_exists(data, item):
    return item in data
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    item1 = 5
    result1 = item_exists(list1, item1)
    print(f"List: {list1}, Item: {item1}, Exists: {result1}")
    list2 = ['a', 'b', 'c', 'd']
    item2 = 'd'
    result2 = item_exists(list2, item2)
    print(f"List: {list2}, Item: {item2}, Exists: {result2}")
    list3 = [10, 20, 30]
    item3 = 5
    result3 = item_exists(list3, item3)
    print(f"List: {list3}, Item: {item3}, Exists: {result3}")
    large_list = list(range(1000000))
    item4 = 999999
    result4 = item_exists(large_list, item4)
    print(f"Large List Check, Item: {item4}, Exists: {result4}")
    large_list_miss = list(range(1000000))
    item5 = 1000000
    result5 = item_exists(large_list_miss, item5)
    print(f"Large List Miss Check, Item: {item5}, Exists: {result5}")