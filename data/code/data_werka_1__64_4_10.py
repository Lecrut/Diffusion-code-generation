def find_last_index(data, value):
    def validate_input():
        if not isinstance(data, list):
            raise ValueError("The first argument must be a list.")
        if not isinstance(value, (int, float, str)):
            raise ValueError("The second argument must be an int, float, or str.")
    
    validate_input()
    last_index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            last_index = i
            break
    return last_index

if __name__ == '__main__':
    list1 = [3, 6, 9, 6, 12, 6]
    value1 = 6
    result1 = find_last_index(list1, value1)
    print(f"List: {list1}, Value: {value1}, Last Index: {result1}")
    
    list2 = ['a', 'b', 'c', 'b', 'd']
    value2 = 'b'
    result2 = find_last_index(list2, value2)
    print(f"List: {list2}, Value: {value2}, Last Index: {result2}")
    
    list3 = [1.5, 2.5, 3.5, 2.5]
    value3 = 2.5
    result3 = find_last_index(list3, value3)
    print(f"List: {list3}, Value: {value3}, Last Index: {result3}")
    
    list4 = [10, 20, 30, 40]
    value4 = 50
    result4 = find_last_index(list4, value4)
    print(f"List: {list4}, Value: {value4}, Last Index: {result4}")