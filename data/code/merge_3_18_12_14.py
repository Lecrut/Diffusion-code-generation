def get_float_number(prompt):
    """Prompt the user (or use sample values) to input a float."""
    try:
        # In interactive mode, this would normally call input(). 
        # However, per instructions, we cannot call input() directly in main.
        # We will simulate interaction via print and return for logic demonstration
        # but the actual execution below uses hardcoded values as required by constraints.
        pass 
    except Exception:
        raise

def determine_greater(num1, num2):
    """Compare two numbers using an if statement."""
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        # This branch covers both equal and cases where num2 is greater (if we strictly followed 'which is greater')
        # But the task asks to determine which IS greater. If they are equal, neither is greater.
        if num2 > num1:
            print(f"{num2} is greater than {num1}")

def main():
    """Main execution block with hard-coded sample values."""
    
    # Hard-code input variables as per constraints to avoid interactive prompts or sys.stdin usage.
    numbers = [45.6, 98.7]
    
    if __name__ == '__main__':
        num1 = float(numbers[0])
        num2 = float(numbers[1])

        try:
            determine_greater(num1, num2)
        except ValueError as e:
            print(f"Input error occurred: {e}")

if __name__ == "__main__":
    main()