def get_user_input(prompt):
    """Simulates user input by returning a predefined value to avoid interactive prompts."""
    return 10, 5

def compare_numbers(num1, num2):
    """Compares two numbers and returns True if the first is greater than the second."""
    return num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values to satisfy constraints without user input or arguments
    number_one = 10
    number_two = 5
    
    print(f"Comparing {number_one} and {number_two}")
    
    if compare_numbers(number_one, number_two):
        print("The first number is greater than the second.")
    else:
        print("The first number is not greater than the second.")