def item_exists(data, item):
    if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
        raise ValueError("Data must be a list of strings")
    return item in set(data)

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    item1 = 'banana'
    result1 = item_exists(list1, item1)
    print(f"List: {list1}, Item: {item1}, Exists: {result1}")

    list2 = ['cat', 'dog', 'elephant']
    item2 = 'fish'
    result2 = item_exists(list2, item2)
    print(f"List: {list2}, Item: {item2}, Exists: {result2}")

    list3 = ['red', 'green', 'blue']
    item3 = 'green'
    result3 = item_exists(list3, item3)
    print(f"List: {list3}, Item: {item3}, Exists: {result3}")

    empty_list = []
    item4 = 'orange'
    try:
        result4 = item_exists(empty_list, item4)
        print(f"List: {empty_list}, Item: {item4}, Exists: {result4}")
    except ValueError as e:
        print(e)

    list5 = ['apple', 123, 'cherry']
    item5 = 'apple'
    try:
        result5 = item_exists(list5, item5)
        print(f"List: {list5}, Item: {item5}, Exists: {result5}")
    except ValueError as e:
        print(e)