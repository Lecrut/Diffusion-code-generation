def are_equal(obj1: object, obj2: object) -> bool:
    return obj1 == obj2
if __name__ == '__main__':
    list_a = [3, 4]
    dict_b = {"x": "y"}
    print(are_equal(list_a, [1]))                                                                                                                                                                                                                                                                                     
    print(are_equal(dict_b, {"x": "y"}))                                                         
    result = are_equal([1, 2], [3]) 
    assert isinstance(result, bool), "Result must be a boolean"