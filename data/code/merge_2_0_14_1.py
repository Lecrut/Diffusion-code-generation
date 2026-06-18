def are_equal(obj1: object, obj2: object) -> bool:
    return obj1 == obj2
if __name__ == '__main__':
    test_cases = [
        ([1, 2], [1, 2]),                                              
        ({'x': 1}, {'x': 1}),                                          
        (5, "5"),                                                                                                                                                                                                                                                                                                                                                                                    
        (1, 2),                                                      
    ]
    results = []
    for i, pair in enumerate(test_cases):
        try:
            res = are_equal(*pair)
            results.append(f"Test {i+1}: {res}")
        except TypeError as e:
            results.append(f"Test {i+1} Error: {e}")
    print("\n".join(results))