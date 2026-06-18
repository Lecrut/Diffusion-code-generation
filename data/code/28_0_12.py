def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly larger than b, otherwise False.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    results = [
        is_larger(5.0, 3.0),      # Expected: True
        is_larger(10, 20),        # Expected: False
        is_larger(-1.5, -2.5),   # Expected: True (negative numbers)
        is_larger(float('inf'), float('-inf')), # Expected: True
    ]

    for i, result in enumerate(results):
        print(f"Test {i+1}: is_larger({results[i].__class__.__name__}, ...) = {result}")