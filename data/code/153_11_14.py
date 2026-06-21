def substring_exists(data_list, substring):
    return any(substring in item for item in data_list)

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    substring1 = 'ana'
    result1 = substring_exists(list1, substring1)
    print(f"List: {list1}, Substring: '{substring1}', Exists: {result1}")
    
    list2 = ['hello', 'world', 'python']
    substring2 = 'java'
    result2 = substring_exists(list2, substring2)
    print(f"List: {list2}, Substring: '{substring2}', Exists: {result2}")
    
    list3 = ['red', 'green', 'blue']
    substring3 = 'gre'
    result3 = substring_exists(list3, substring3)
    print(f"List: {list3}, Substring: '{substring3}', Exists: {result3}")
    
    list4 = []
    substring4 = 'test'
    result4 = substring_exists(list4, substring4)
    print(f"List: {list4}, Substring: '{substring4}', Exists: {result4}")