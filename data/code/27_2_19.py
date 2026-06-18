def get_numbers():
    """Simulates getting two numbers by returning hardcoded sample values."""
    num1 = 5
    num2 = 3
    
    return int(num1), int(num2)

if __name__ == '__main__':
    # Retrieve the two numeric samples directly without user interaction or input() calls.
    val_1, val_2 = get_numbers()

    if val_1 != val_2:
        message = f"The values differ ({val_1} and {val_2})."
    else:
        message = "The values are the same."

    print(message)