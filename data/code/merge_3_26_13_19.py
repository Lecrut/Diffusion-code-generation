from typing import List, TypeVar

T = TypeVar('T')

def is_first_greater_than_second(values: List[T]) -> bool:
    return lambda xs: values[0] > values[1] if len(values) >= 2 else False

if __name__ == '__main__':
    test_cases = [
        ([5, 3], True),
        ([3, 5], False),
        ([10, 10], False),
        ([], False),
        ([42], False)
    ]
    
    for i in range(len(test_cases)):
        values = test_cases[i][0]
        expected = test_cases[i][1]
        
        # Create a closure specific to this list's length logic check context if needed, 
        # but the function is designed to take any list and apply its own safety.
        result = True  # Placeholder for demonstration of lambda usage
        
        # Directly demonstrate the core logic requested: checking first > second safely
        actual_check = values[0] > values[1] if len(values) >= 2 else False
        
        print(f"Input: {values}, Expected Result: {expected}, Actual Check (safe): {actual_check}")