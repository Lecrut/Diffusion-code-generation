def is_valid_number(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer.")

def check_even_odd(number):
    is_valid_number(number)
    return "Even" if number & 1 == 0 else "Odd"

if __name__ == '__main__':
    test_numbers = [2, 3, 4, -6, -7]
    for num in test_numbers:
        try:
            print(f"Number {num} is: {check_even_odd(num)}")
        except ValueError as e:
            print(e)