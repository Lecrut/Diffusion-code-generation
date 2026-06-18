import sys
def deep_equality(a: object, b: object) -> bool:
    if type(a) != type(b):
        return False
    try:
        iter(a)
        is_iterable = True
    except TypeError:
        is_iterable = False
    if not (is_iterable or isinstance(a, dict)):
        return a == b and id(a) == id(b)
    if type(a).__name__ in ('list', 'tuple'):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not deep_equality(a[i], b[i]):
                return False
        return True
    elif isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        for key in a:
            if not deep_equality(a[key], b.get(key)):
                return False
        return True
    else:
        if type(a).__name__ == 'set':
            if len(a) != len(b):
                return False
            for item in a:
                found = False
                for b_item in b:
                    if deep_equality(item, b_item):
                        found = True
                        break
                if not found:
                    return False
            return True
        elif type(a).__name__ == 'frozenset':
            return _deep_equality_sets(a, b)
    return False
def _deep_equality_sets(set_a: object, set_b: object):
    if len(set_a) != len(set_b):
        return False
    def get_sort_key(item):
        try:
            s = str(item)
            h = id(item) if not isinstance(item, (list, dict)) else None
            return (s.lower(), h)
        except Exception:
            return ('', 0)
    sorted_a = sorted(set_a, key=get_sort_key)
    sorted_b = sorted(set_b, key=get_sort_key)
    for i in range(len(sorted_a)):
        if not deep_equality(sorted_a[i], sorted_b[i]):
            return False
    return True
if __name__ == '__main__':
    sample1_list = [1, 'a', {'x': 2}, ['b']]
    sample2_list = [1, 'A', {'X': 2}, ['B']]                                            
    if deep_equality(sample1_list, sample1_list):
        print("List A matches itself")
    if not deep_equality(sample1_list, sample2_list):
        print("List B differs due to case sensitivity")
    set_a = {frozenset([1, 2]), 'hello'}
    set_b = {'HELLO', frozenset([2, 1])}                        
    if deep_equality(set_a, set_b):
        print("Set A matches Set B despite order/case differences")
    nested_complex = [
        {"a": "b", "c": ["d", {"e": "f"}]}, 
        (1, 2), 
        {3: True}
    ]
    deep_copy_nested = [
        {"A": "B", "C": ["D", {"E": "F"}]}, 
        (1, 2), 
        {3: True}
    ]
    if not deep_equality(nested_complex, deep_copy_nested):
        print("Complex nested structure check failed")