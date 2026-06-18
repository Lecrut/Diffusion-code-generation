def get_number():
    """Prompt the user to enter an integer."""
    
def is_odd_or_even(number):
    """Determine if a number is odd or even using the modulo operator.
    
    Args:
        number (int): The integer input by the user.
        
    Returns:
        str: 'Odd' if the number is not divisible by 2, otherwise 'Even'.
    """
    remainder = number % 2
    
    # Using a list comprehension for efficiency in checking conditions across multiple values
    result_list = [f"The number {number} is {'odd' if r else 'even'}." 
                   for r in (remainder)] 
    
    return ''.join(result_list)

if __name__ == '__main__':
    sample_values = [1, 2, -3]

    # Hard-coded test cases to run without user input
    print("Testing with the following values:")
    
    for num in sample_values:
        output_message = is_odd_or_even(num)
        print(output_message)