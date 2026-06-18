def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_numbers = [1, 2, -3, 4]

    for num in test_numbers:
        result = is_even(num)
        status = "even" if result else "odd"
        print(f"{num} is {status}.")