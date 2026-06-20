def is_odd(number):
    try:
        if not isinstance(number, int):
            raise ValueError("Input must be an integer")
        return number % 2 == 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == '__main__':
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for num in test_numbers:
        print(f"{num} is odd: {is_odd(num)}")