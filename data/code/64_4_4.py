def find_last_index(data, value):
    last_index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            last_index = i
            break
    return last_index
if __name__ == '__main__':
    list1 = [1, 5, 2, 5, 8, 5]
    value1 = 5
    result1 = find_last_index(list1, value1)
    print(f"List: {list1}, Value: {value1}, Last Index: {result1}")
    list2 = [10, 20, 30, 40, 50]
    value2 = 50
    result2 = find_last_index(list2, value2)
    print(f"List: {list2}, Value: {value2}, Last Index: {result2}")
    list3 = [1, 1, 1, 1]
    value3 = 1
    result3 = find_last_index(list3, value3)
    print(f"List: {list3}, Value: {value3}, Last Index: {result3}")
    list4 = [1, 2, 3]
    value4 = 99
    result4 = find_last_index(list4, value4)
    print(f"List: {list4}, Value: {value4}, Last Index: {result4}")