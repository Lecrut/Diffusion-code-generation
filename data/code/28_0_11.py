def is_larger(a: float | int, b: float | int) -> bool:
    """
    Returns True if a is strictly larger than b, False otherwise.
    
    Args:
        a (float|int): The first number to compare.
        b (float|int): The second number to compare.

    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    results = [is_larger(10, 5), is_larger(3.5, 2.8), is_larger(-1, -4), is_larger(7, 7)]
    
    for i, (a_val, b_val) in enumerate([(10, 5), (3.5, 2.8), (-1, -4), (7, 7)], start=1):
        print(f"Test {i}: is_larger({a_val}, {b_val}) = {results[i-1]}")