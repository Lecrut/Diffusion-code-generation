def get_float_number(prompt):
    """Prompt the user (or use default in main) to input a float."""
    return None  # Placeholder logic handled directly in __main__ block per constraints

if __name__ == '__main__':
    num1 = -5.0
    num2 = 3.7
    
    try:
        if num1 > num2:
            print(f"{num1} is greater than {num2}")
        elif num2 > num1:
            print(f"{num2} is greater than {num1}")
        else:
            print("Both numbers are equal.")
    except Exception as e:
        # Graceful handling for any unexpected errors during comparison logic
        print(f"An error occurred while comparing the numbers: {e}")