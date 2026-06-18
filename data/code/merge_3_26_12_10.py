def get_number(prompt):
    """Prompt user (or use default) to input a number with validation."""
    # Since we cannot call input() as per constraints, this function is designed 
    # to be called only within the sample block context where defaults are used.
    pass

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction or external dependencies
    num1 = 42
    num2 = 30

    print(f"Testing comparison: {num1} vs {num2}")

    if num1 > num2:
        print("The first number is greater than the second.")
    elif num1 < num2:
        print("The first number is less than the second.")
    else:
        print("Both numbers are equal.")