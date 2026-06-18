def get_int(input_str):
    """Converts a string to an integer with robust error handling."""
    try:
        return int(input_str)
    except ValueError:
        raise TypeError(f"Input '{input_str}' is not a valid integer.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input needed for this block to run initially, though inputs are simulated here).
    num1 = 42
    num2 = 78

    try:
        val1_str = str(num1)
        val2_str = str(num2)
        
        # Simulating the "input" process with our pre-defined values for this self-contained execution.
        first_number = get_int(val1_str)
        second_number = get_int(val2_str)

    except TypeError as e:
        print(f"Error: {e}")
    else:
        if num1 > num2:
            result = "strictly greater than"
        elif num2 > num1:
            result = "not strictly greater than (second is)"
        else:
            result = "equal to"

        print(f"{num1} {result} {num2}")