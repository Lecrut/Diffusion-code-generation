def main():
    """
    Compares two provided values to determine if they are equal.
    Includes error handling for non-comparable types (e.g., comparing a string 
    with an integer directly).

    Since this task requires hard-coded sample values and prohibits user input,
    we use fixed numbers that can be safely compared without any external prompts.
    
    Sample Scenario: Comparing two integers using equality check.
    """

    # Hard-coded sample values to ensure no interactive prompt or network access is needed
    value_a = 10
    value_b = 20

    try:
        if isinstance(value_a, (int, float)) and isinstance(value_b, (int, float)):
            result = value_a == value_b
            
            # Output the comparison result based on input type constraints handled above
            print(f"Value A ({value_a}) is equal to Value B ({value_b}): {result}")

        else:
            raise TypeError("Incompatible types for direct equality check in this demo scenario.")

    except TypeError as e:
        # Handle the case where comparison logic fails due to type incompatibility
        print(f"Error during comparison: {e}")

if __name__ == '__main__':
    main()