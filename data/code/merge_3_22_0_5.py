def is_odd_or_even(number):
    """
    Determines if a given integer is odd or even.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: A message indicating whether the number is odd or even.
    """
    remainder = number % 2
    return "even" if remainder == 0 else "odd"

if __name__ == "__main__":
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [1, -4, 7, 0]

    for num in samples:
        result_message = is_odd_or_even(num)
        print(f"The number {num} is {result_message}.")