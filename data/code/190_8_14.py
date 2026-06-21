def validate_input(data_list, item):
    if not isinstance(data_list, list):
        raise ValueError("First argument must be a list")
    if not isinstance(item, (str, int)):
        raise ValueError("Second argument must be a string or an integer")

def check_membership(data_list, item):
    validate_input(data_list, item)
    return any(substring in str(element) for element in data_list)

if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry']
    substring1 = 'an'
    print(f"List: {list1}, Substring: '{substring1}'")
    print(f"Substring exists: {check_membership(list1, substring1)}")
    
    list2 = [10, 20, 30, 40]
    substring2 = '5'
    print(f"\nList: {list2}, Substring: '{substring2}'")
    print(f"Substring exists: {check_membership(list2, substring2)}")
    
    list3 = ['hello world', 'python programming']
    substring3 = 'world'
    print(f"\nList: {list3}, Substring: '{substring3}'")
    print(f"Substring exists: {check_membership(list3, substring3)}")