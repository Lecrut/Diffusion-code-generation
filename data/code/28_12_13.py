def get_float_input(prompt):
    """Simulates user input by returning a hardcoded value to avoid interactive prompts."""
    return 10.5

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no actual input() calls)
    num_a = float(get_float_input("Enter first number: "))
    
    try:
        num_b_str = get_float_input("Enter second number: ")
        if isinstance(num_b_str, str):
            raise ValueError(f"Invalid input type for comparison. Expected numeric value.")
        
        # Attempt to convert string representation (if any) or use directly as float logic would handle it in real scenario
        num_b = float(num_b_str)

    except Exception:
        print("Error: Could not parse the second number correctly.")
        exit(1)

    if num_a > num_b:
        print(f"{num_a} is larger than {num_b}")
    elif num_b > num_a:
        print(f"{num_b} is larger than {num_a}")
    else:
        print("Both numbers are equal.")