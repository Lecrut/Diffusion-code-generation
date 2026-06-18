def is_even(number):
    """
    Determines if a given integer is even.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

def main():
    # Sample values for testing without user input or command-line arguments
    sample_values = [10, -3, 42, 0]

    print("Testing numbers to determine if they are even or odd:")
    
    for num in sample_values:
        result = is_even(num)
        status = "even" if result else "odd"
        print(f"{num} is {status}")

if __name__ == '__main__':
    main()