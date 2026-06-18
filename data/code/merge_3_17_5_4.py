def check_parity(number):
    """Returns 'Even' if number is divisible by 2, otherwise returns 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements to avoid any input prompts or arguments.
    test_numbers = [4, 7, -3, 10]

    for num in test_numbers:
        result = check_parity(num)
        print(result)