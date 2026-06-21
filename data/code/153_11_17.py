def substring_exists(data, substring):
    return substring in data

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    substring1 = 'an'
    result1 = substring_exists(list1, substring1)
    print(f"List: {list1}, Substring: '{substring1}', Exists: {result1}")

    list2 = ['hello', 'world', 'python']
    substring2 = 'java'
    result2 = substring_exists(list2, substring2)
    print(f"List: {list2}, Substring: '{substring2}', Exists: {result2}")

    list3 = ['a', 'ab', 'abc', 'abcd']
    substring3 = 'bc'
    result3 = substring_exists(list3, substring3)
    print(f"List: {list3}, Substring: '{substring3}', Exists: {result3}")

    empty_list = []
    substring4 = 'empty'
    result4 = substring_exists(empty_list, substring4)
    print(f"List: {empty_list}, Substring: '{substring4}', Exists: {result4}")