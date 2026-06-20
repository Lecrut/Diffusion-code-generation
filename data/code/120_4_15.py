def are_values_identical(val1, val2):
    if type(val1) != type(val2):
        return False
    
    if isinstance(val1, (int, float, str)):
        return val1 == val2
    
    if isinstance(val1, list):
        if len(val1) != len(val2):
            return False
        for item1, item2 in zip(val1, val2):
            if not are_values_identical(item1, item2):
                return False
        return True
    
    if isinstance(val1, dict):
        if len(val1) != len(val2):
            return False
        for key in val1:
            if key not in val2 or not are_values_identical(val1[key], val2[key]):
                return False

if __name__ == '__main__':
    sample1 = [1, 2, {'a': 3}]
    sample2 = [1, 2, {'a': 3}]
    print(are_values_identical(sample1, sample2))
    
    sample3 = [1, 2, {'a': 4}]
    print(are_values_identical(sample1, sample3))