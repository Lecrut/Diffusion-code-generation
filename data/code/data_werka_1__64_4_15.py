def find_last_index(data, value):
    index_map = {}
    for i in range(len(data)):
        if data[i] == value:
            index_map[value] = i
    return index_map.get(value, -1)

if __name__ == '__main__':
    list1 = [3, 5, 2, 5, 8, 5]
    value1 = 5
    result1 = find_last_index(list1, value1)
    print(f"List: {list1}, Value: {value1}, Last Index: {result1}")

    list2 = [7, 10, 30, 10, 40]
    value2 = 10
    result2 = find_last_index(list2, value2)
    print(f"List: {list2}, Value: {value2}, Last Index: {result2}")

    list3 = [1, 2, 3, 4, 5]
    value3 = 99
    result3 = find_last_index(list3, value3)
    print(f"List: {list3}, Value: {value3}, Last Index: {result3}")