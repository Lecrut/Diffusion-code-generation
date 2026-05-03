def are_equal(a, b):
    if type(a) != type(b):
        return False
    if isinstance(a, dict):
        if len(a) != len(b):
            return False
        for key in a:
            if key not in b:
                return False
            if not are_equal(a[key], b[key]):
                return False
        return True
    elif isinstance(a, list):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not are_equal(a[i], b[i]):
                return False
        return True
    else:
        return a == b
if __name__ == '__main__':
    list1 = [1, [2, 3], {'a': 4}]
    list2 = [1, [2, 3], {'a': 4}]
    list3 = [1, [2, 4], {'a': 4}]
    list4 = [1, [2, 3], {'a': 5}]
    list5 = [1, [2, 3]]
    list6 = [1, [2, 3, 4]]
    dict1 = {'a': 1, 'b': [2, 3]}
    dict2 = {'a': 1, 'b': [2, 3]}
    dict3 = {'a': 1, 'b': [2, 4]}
    dict4 = {'a': 1, 'b': [2, 3, 4]}
    dict5 = {'a': 1}
    print(f"list1 == list2: {are_equal(list1, list2)}")
    print(f"list1 == list3: {are_equal(list1, list3)}")
    print(f"list1 == list4: {are_equal(list1, list4)}")
    print(f"list1 == list5: {are_equal(list1, list5)}")
    print(f"list1 == list6: {are_equal(list1, list6)}")
    print(f"dict1 == dict2: {are_equal(dict1, dict2)}")
    print(f"dict1 == dict3: {are_equal(dict1, dict3)}")
    print(f"dict1 == dict4: {are_equal(dict1, dict4)}")
    print(f"dict1 == dict5: {are_equal(dict1, dict5)}")