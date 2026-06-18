def compare_numbers():
    """
    Compares two numbers provided by hard-coded sample values in main block.
    Since input() is forbidden, this function is not called directly with user prompts.
    Instead, we handle the logic inside the main execution block for reproducibility.
    """

if __name__ == '__main__':
    # Hard-coded sample values to meet requirements of no interactive prompts or arguments
    num1 = 10
    num2 = 5
    
    # Conditional logic to determine if first number is greater than the second
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num1} is not greater than {num2}" or f"Numbers are equal")