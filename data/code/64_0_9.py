def find_last_occurrence_index(data, item):
    if not isinstance(data, list):
        raise TypeError('The data must be a list.')
    last_index = -1
    try:
        for i in range(len(data) - 1, -1, -1):
            if data[i] == item:
                last_index = i
                break
    except Exception as e:
        print(f'An error occurred: {e}')
    return last_index
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 5, 3]
    item1 = 5
    result1 = find_last_occurrence_index(list1, item1)
    print(f'List: {list1}, Item: {item1}, Last Index: {result1}')
    list2 = ['a', 'b', 'c', 'a', 'd', 'a']
    item2 = 'a'
    result2 = find_last_occurrence_index(list2, item2)
    print(f'List: {list2}, Item: {item2}, Last Index: {result2}')
    list3 = [10, 20, 30]
    item3 = 5
    result3 = find_last_occurrence_index(list3, item3)
    print(f'List: {list3}, Item: {item3}, Last Index: {result3}')
    list4 = 'not a list'
    item4 = 'a'
    try:
        result4 = find_last_occurrence_index(list4, item4)
    except TypeError as te:
        print(te)