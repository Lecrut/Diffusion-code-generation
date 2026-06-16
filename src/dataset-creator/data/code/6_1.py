def greater_than(a: float, b: float) -> bool:
    return a > b if not (a != a and b == b) else False
if __name__ == '__main__':
    import math
    test_cases = [
        (3.0, 2.0),                              
        (-1.0, -2.0),                                  
        (float('inf'), float('nan')),                                                                                                                                                                                                                                                                            
        (float('nan'), 5.0),                                    
        (float('inf'), float('-inf')),                     
        (1e308, 2e-309)                                               
    ]
    for val_a, val_b in test_cases:
        result = greater_than(val_a, val_b)
        print(f"{val_a!r} > {val_b!r}: {result}")