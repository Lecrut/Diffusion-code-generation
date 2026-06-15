def check_existence(data, value):
    for item in data:
        if item == value:
            yield True
            return
    yield False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    value1 = 3
    print(f"List: {list1}, Value: {value1}")
    for result in check_existence(list1, value1):
        print(result)
    list2 = [10, 20, 30]
    value2 = 5
    print(f"\nList: {list2}, Value: {value2}")
    for result in check_existence(list2, value2):
        print(result)
    list3 = ['a', 'b', 'c']
    value3 = 'd'
    print(f"\nList: {list3}, Value: {value3}")
    for result in check_existence(list3, value3):
        print(result)