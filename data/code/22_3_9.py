# Check if an integer is odd using modulo operator
is_odd = num % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_numbers = [17, -5, 30]
    for n in test_numbers:
        print(f"{n} is odd" if (n % 2 != 0) else f"{n} is even")