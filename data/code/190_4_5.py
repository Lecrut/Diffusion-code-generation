def check_existence(data, value):
    for item in data:
        if item == value:
            yield True
            return
    yield False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    value1 = 3
    print(f"List: {list1}, Value: {value1} -> Result: {list(check_existence(list1, value1))}")
    list2 = [10, 20, 30]
    value2 = 5
    print(f"List: {list2}, Value: {value2} -> Result: {list(check_existence(list2, value2))}")
    list3 = ['a', 'b', 'c']
    value3 = 'd'
    print(f"List: {list3}, Value: {value3} -> Result: {list(check_existence(list3, value3))}")
    list4 = [1, 2, 1]
    value4 = 1
    print(f"List: {list4}, Value: {value4} -> Result: {list(check_existence(list4, value4))}")