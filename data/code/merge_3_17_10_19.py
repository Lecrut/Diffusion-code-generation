def check_parity(number):
    """
    Determines if a number is even or odd using the modulo operator.
    
    Args:
        number (int): The integer to be checked.
        
    Returns:
        str: 'even' if divisible by 2, otherwise 'odd'.
    """
    return "even" if number % 2 == 0 else "odd"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements to avoid interactive prompts.
    test_values = [4, 7, -3, 10]

    for num in test_values:
        result = check_parity(num)
        print(f"{num} is {result}.")