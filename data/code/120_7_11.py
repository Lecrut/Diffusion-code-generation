def is_identical(obj1, obj2):
    return obj1 == obj2

if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'b': 2}
    dict3 = {'a': 1, 'b': 3}
    
    result1 = is_identical(dict1, dict2)
    print(f"dict1 is identical to dict2: {result1}")
    
    result2 = is_identical(dict1, dict3)
    print(f"dict1 is identical to dict3: {result2}")