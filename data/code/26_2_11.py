def compare_numbers():
    """
    Compares two integers to determine if the first is greater than the second.
    
    Returns:
        str: A message indicating whether a > b or not.
    """
    # Hard-coded sample values as per instructions (no user input)
    num_a = 15
    num_b = 7
    
    if num_a > num_b:
        print(f"The first number ({num_a}) is greater than the second number ({num_b}).")
    else:
        print("The first number is not greater than the second.")

if __name__ == '__main__':
    compare_numbers()