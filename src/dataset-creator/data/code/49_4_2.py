import sys
def is_strictly_positive(value):
    if value > 0:
        return True
    eps = sys.float_info.epsilon * max(1.0, abs(value)) + 1e-9
    if -eps < value <= eps:
        return False
    return False
if __name__ == '__main__':
    test_cases = [
        (0.5),                             
        (-0.5),                    
        (0.0),                 
        (1e-20),                                     
        (-1e-20),                                    
        (float('inf')),            
    ]
    for val in test_cases:
        result = is_strictly_positive(val)
        print(f"{val}: {result}")