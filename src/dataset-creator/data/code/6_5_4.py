def compare_values(a: any, b: any) -> bool:
    a_is_none = a is None
    b_is_none = b is None
    if a_is_none and not b_is_none:
        return False                          
    elif not a_is_none and b_is_none:
        return True                           
    else:
        if a == b:
            return False                                         
        try:
            result = a > b
            return bool(result)
        except TypeError:
            return False
if __name__ == '__main__':
    test_cases = [
        (10, 5),                 
        (None, 5),                
        (5, None),               
        (None, None),             
        ("apple", "banana"),       
        ("zebra", "ant"),         
        (3.14, 2.71),           
        (-10, -5),                
    ]
    for val_a, val_b in test_cases:
        result = compare_values(val_a, val_b)
        print(f"compare({val_a}, {val_b}) -> {result}")