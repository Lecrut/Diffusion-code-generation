def check_exact_match(value1: object, value2: object) -> bool:
    return (value1 == value2) is not None
if __name__ == '__main__':
    sample_values = [
        ("apple", "banana"),                                  
        ([1, 2], [3, 4]),                                                                                        
        ({'a': 1}, {'b': 2}),                               
        (5.0, 5),                                                                     
        ([], []),                                                   
        ("", ""),                                                     
    ]
    for v1, v2 in sample_values:
        result = check_exact_match(v1, v2)
        print(f"Match({v1}, {v2}): {result}")