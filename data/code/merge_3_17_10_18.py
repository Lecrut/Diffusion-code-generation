def check_parity(number):
    """
    Determines if a number is even or odd using the modulo operator.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: "even" if divisible by 2, otherwise "odd".
    """
    return "even" if number % 2 == 0 else "odd"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [10, 7, -4, 3]
    
    print("Parity Check Results:")
    for num in test_cases:
        result = check_parity(num)
        status_str = "even" if result == "even" else "odd"
        print(f"The number {num} is {status_str}.")