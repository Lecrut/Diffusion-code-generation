def check_difference():
    """
    Compares two numbers to determine if they differ.
    
    Returns:
        bool: True if the numbers are different, False otherwise.
    """
    # Hard-coded sample values as per requirements (no user input)
    num1 = 42
    num2 = 98
    
    return num1 != num2

if __name__ == '__main__':
    result = check_difference()
    
    if result:
        print("The two entered values differ.")
    else:
        print("The two entered values are the same.")