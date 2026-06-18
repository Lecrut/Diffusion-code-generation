def check_number(n: int) -> str:
    """Returns a descriptive string indicating if n is negative."""
    if n < 0:
        return f"The number {n} is negative."
    else:
        return f"The number {n} is not negative."

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or network access.
    test_values = [-5, 0, 10]

    for value in test_values:
        result_message = check_number(value)
        print(result_message)