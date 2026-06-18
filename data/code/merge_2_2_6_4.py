import math
def is_positively_signed(value: float) -> bool:
    if value == 0:
        return False
    return value > math.nextafter(0.0, -1)
if __name__ == '__main__':
    test_cases = [
        2.5,
        -3e-40,
        float('inf'),
        float('-inf'),
        1e-324,                                                                                
        math.nextafter(0.0, -1),                  
    ]
    for val in test_cases:
        result = is_positively_signed(val)
        print(f"Value: {val}, Is Positive: {result}")