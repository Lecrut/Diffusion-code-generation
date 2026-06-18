def is_strictly_greater(number1: float, number2: float) -> bool:
    """Check if the first strictly greater than the second."""
    return number1 > number2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or network access is required.
    num_a = 40.578936
    num_b = -90

    result = is_strictly_greater(num_a, num_b)
    
    print(f"Is {num_a} strictly greater than {num_b}?")
    if result:
        print("Yes.")
    else:
        print("No.")