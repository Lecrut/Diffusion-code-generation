# Check if 'num' is even using a one-liner expression
is_even = num % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or network access
    for val in [1, 2, -4, 0]:
        print(f"Is {val} even? {is_even := (val % 2 == 0)}")