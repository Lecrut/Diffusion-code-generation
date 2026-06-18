def get_remainder_and_parity(n: int) -> tuple[int, str]:
    """
    Returns a tuple containing (remainder, parity_string).
    
    Args:
        n (int): The integer input to evaluate
        
    Returns:
        tuple: A tuple where the first element is remainder modulo 2 
               and the second element is "odd" or "even".
    """
    remainder = n % 2
    if remainder == 0:
        parity_str = "even"
    else:
        parity_str = "odd"
    
    return (remainder, parity_str)

if __name__ == '__main__':
    # Hard-coded sample values to test the function
    samples = [15, -32, 0, 7]
    
    for num in samples:
        remainder, result_type = get_remainder_and_parity(num)
        print(f"Number: {num}, Remainder ({'mod 2'}): {remainder} -> Is {result_type}")