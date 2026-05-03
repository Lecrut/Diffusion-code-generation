def find_last_index(data, value):
    last_index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            last_index = i
            break
    return last_index
if __name__ == '__main__':
    list1 = [1, 2, 3, 2, 4, 2]
    value1 = 2
    result1 = find_last_index(list1, value1)
    print(f"List: {list1}, Value: {value1}, Last Index: {result1}")
    list2 = [10, 20, 30, 20, 40]
    value2 = 20
    result2 = find_last_index(list2, value2)
    print(f"List: {list2}, Value: {value2}, Last Index: {result2}")
    list3 = [5, 5, 5, 5]
    value3 = 5
    result3 = find_last_index(list3, value3)
    print(f"List: {list3}, Value: {value3}, Last Index: {result3}")
    list4 = [1, 2, 3]
    value4 = 99
    result4 = find_last_index(list4, value4)
    print(f"List: {list4}, Value: {value4}, Last Index: {result4}")
    list5 = []
    value5 = 1
    result5 = find_last_index(list5, value5)
    print(f"List: {list5}, Value: {value5}, Last Index: {result5}")