def is_odd(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    return number % 2 != 0

if __name__ == '__main__':
    test_numbers = [5, -10, 0, 3, -7]
    for num in test_numbers:
        print(f"{num} is odd: {is_odd(num)}")