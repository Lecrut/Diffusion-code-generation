import json
def deep_equality_check(obj1: any, obj2: any) -> bool:
    if type(obj1) != type(obj2):
        return False
    try:
        iter(obj1)
    except TypeError:
        return obj1 == obj2
    if isinstance(obj1, (list, tuple)):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not deep_equality_check(obj1[i], obj2[i]):
                return False
        return True
    if isinstance(obj1, dict):
        if set(obj1.keys()) != set(obj2.keys()):
            return False
        for key in obj1:
            if not deep_equality_check(obj1[key], obj2.get(key)):
                return False
        return True
    try:
        set_obj = {tuple(sorted(v)) for v in obj1} if isinstance(obj1, set) else list(obj1)
        other_set = {tuple(sorted(v)) for v in obj2} if isinstance(obj2, set) else list(obj2)
        if isinstance(obj1, set):
            return len(set_obj) == len(other_set) and all(deep_equality_check(item_a, item_b) 
                                                           for item_a in obj1 
                                                           for item_b in other_set 
                                                           if deep_equality_check(item_a, item_b))
    except TypeError:
        pass
    return obj1 == obj2
if __name__ == '__main__':
    sample_data_1 = [
        {"a": 1, "b": [3, 4], "c": (5, 6)},
        {1: "x", 2: ["y", "z"]}
    ]
    sample_data_2 = [
        {"a": 1, "b": [3, 4], "c": (5, 6)},
        {1: "x", 2: ["y", "z"]}
    ]
    sample_data_3 = [
        {"a": 1, "b": [3, 4]},
        {1: "x", 2: ["y", "z"]}
    ]
    print(deep_equality_check(sample_data_1, sample_data_2))       
    print(deep_equality_check(sample_data_1, sample_data_3))