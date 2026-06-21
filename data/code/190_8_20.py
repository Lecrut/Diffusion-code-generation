def substring_exists(data_list, sub):
    return any(sub in element for element in data_list)

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    sub1 = 'an'
    print(f"List: {list1}, Substring: '{sub1}'")
    print(f"Substring exists: {substring_exists(list1, sub1)}")

    list2 = ['hello', 'world', 'python']
    sub2 = 'java'
    print(f"\nList: {list2}, Substring: '{sub2}'")
    print(f"Substring exists: {substring_exists(list2, sub2)}")

    list3 = ['foo', 'bar', 'baz']
    sub3 = 'qux'
    print(f"\nList: {list3}, Substring: '{sub3}'")
    print(f"Substring exists: {substring_exists(list3, sub3)}")