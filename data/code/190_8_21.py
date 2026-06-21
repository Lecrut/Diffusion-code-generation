def substring_exists(data_list, substring):
    return any(substring in element for element in data_list)

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    substring1 = 'an'
    print(f"List: {list1}, Substring: '{substring1}'")
    print(f"Substring exists: {substring_exists(list1, substring1)}")

    list2 = ['hello', 'world', 'python', 'programming']
    substring2 = 'xyz'
    print(f"\nList: {list2}, Substring: '{substring2}'")
    print(f"Substring exists: {substring_exists(list2, substring2)}")