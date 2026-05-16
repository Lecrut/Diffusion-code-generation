class ItemComparer:
    def check_equality(self, a, b):
        if type(a) != type(b):
            return False
        if isinstance(a, dict):
            if len(a) != len(b):
                return False
            for key in a:
                if key not in b:
                    return False
                if not self.check_equality(a[key], b[key]):
                    return False
            return True
        elif isinstance(a, list):
            if len(a) != len(b):
                return False
            for i in range(len(a)):
                if not self.check_equality(a[i], b[i]):
                    return False
            return True
        else:
            return a == b
if __name__ == '__main__':
    comparer = ItemComparer()
    list1 = [1, [2, 3], {'x': 4}]
    list2 = [1, [2, 3], {'x': 4}]
    list3 = [1, [2, 3], {'x': 5}]
    list4 = [1, [2, 3]]
    dict1 = {'a': 1, 'b': [2, 3]}
    dict2 = {'a': 1, 'b': [2, 3]}
    dict3 = {'a': 1, 'b': [2, 4]}
    dict4 = {'a': 1, 'c': 3}
    print(f"list1 == list2: {comparer.check_equality(list1, list2)}")
    print(f"list1 == list3: {comparer.check_equality(list1, list3)}")
    print(f"list1 == list4: {comparer.check_equality(list1, list4)}")
    print("-" * 20)
    print(f"dict1 == dict2: {comparer.check_equality(dict1, dict2)}")
    print(f"dict1 == dict3: {comparer.check_equality(dict1, dict3)}")
    print(f"dict1 == dict4: {comparer.check_equality(dict1, dict4)}")