def find_last_occurrence_index(data_list, item):
    last_index = -1
    for i in range(len(data_list) - 1, -1, -1):
        if data_list[i] == item:
            last_index = i
            break
    return last_index
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 5, 3]
    item1 = 5
    result1 = find_last_occurrence_index(list1, item1)
    print(f"List: {list1}, Item: {item1}, Last Occurrence Index: {result1}")
    list2 = [10, 20, 30, 40, 50]
    item2 = 50
    result2 = find_last_occurrence_index(list2, item2)
    print(f"List: {list2}, Item: {item2}, Last Occurrence Index: {result2}")
    list3 = [1, 1, 1, 1]
    item3 = 1
    result3 = find_last_occurrence_index(list3, item3)
    print(f"List: {list3}, Item: {item3}, Last Occurrence Index: {result3}")
    list4 = [100, 200, 300]
    item4 = 500
    result4 = find_last_occurrence_index(list4, item4)
    print(f"List: {list4}, Item: {item4}, Last Occurrence Index: {result4}")
    list5 = []
    item5 = 10
    result5 = find_last_occurrence_index(list5, item5)
    print(f"List: {list5}, Item: {item5}, Last Occurrence Index: {result5}")
    list6 = [7, 7, 7]
    item6 = 7
    result6 = find_last_occurrence_index(list6, item6)
    print(f"List: {list6}, Item: {item6}, Last Occurrence Index: {result6}")