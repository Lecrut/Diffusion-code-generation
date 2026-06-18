def check_parity(number):
    """
    Determines if a given integer is even or odd.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'even' if the number is divisible by 2, otherwise 'odd'.
    """
    return "even" if number % 2 == 0 else "odd"

def main():
    # Hard-coded sample values for testing without user input or external dependencies.
    test_values = [1, 24, -5, 100]

    print("Testing parity with hard-coded samples:")
    for val in test_values:
        result = check_parity(val)
        status_str = f"{val} is {result}"
        print(status_str)

if __name__ == '__main__':
    main()