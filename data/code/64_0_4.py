def find_last_occurrence_index(data, item):
    last_index = -1
    for i in range(len(data)):
        if data[i] == item:
            last_index = i
    return last_index
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 5, 3]
    item1 = 5
    result1 = find_last_occurrence_index(list1, item1)
    print(f"List: {list1}, Item: {item1}, Last Index: {result1}")
    list2 = ['a', 'b', 'c', 'a', 'd']
    item2 = 'a'
    result2 = find_last_occurrence_index(list2, item2)
    print(f"List: {list2}, Item: {item2}, Last Index: {result2}")
    list3 = [10, 20, 30]
    item3 = 5
    result3 = find_last_occurrence_index(list3, item3)
    print(f"List: {list3}, Item: {item3}, Last Index: {result3}")
    list4 = []
    item4 = 1
    result4 = find_last_occurrence_index(list4, item4)
    print(f"List: {list4}, Item: {item4}, Last Index: {result4}")
    list5 = [7, 7, 7]
    item5 = 7
    result5 = find_last_occurrence_index(list5, item5)
    print(f"List: {list5}, Item: {item5}, Last Index: {result5}")