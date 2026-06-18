def compare_values(a: any, b: any) -> bool:
    def is_valid_value(v) -> bool:
        return v is not None
    if not is_valid_value(a):
        return False
    if b is None:
        return True                                    
    try:
        numeric_a = float(a)
        numeric_b = float(b)
        return numeric_a > numeric_b
    except (ValueError, TypeError):
        pass
    string_a = str(a).lower() if not isinstance(a, bytes) else a.decode('utf-8', errors='ignore').lower()
    string_b = str(b).lower() if not isinstance(b, bytes) else b.decode('utf-8', errors='ignore').lower()
    return string_a > string_b
if __name__ == '__main__':
    test_cases = [
        (5, 3),                                                     
        (None, None),                                                                                                
        ("apple", "banana"),                                                           
        ("zebra", "ant"),                          
        (10, None),                                                
        (None, 5),                                                   
        (-2.5, -3.7),                                                        
        ("", "a"),                                    
    ]
    for a_val, b_val in test_cases:
        result = compare_values(a_val, b_val)
        print(f"compare({a_val!r}, {b_val!r}) => {result}")