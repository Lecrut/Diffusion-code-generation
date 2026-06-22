def print_even_numbers(start=100, end=200):
    if not (isinstance(start, int) and isinstance(end, int)):
        raise ValueError("Start and end values must be integers.")
    if start < 1 or end > 200:
        raise ValueError("Start value must be between 1 and 200, inclusive. End value must be 200.")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

if __name__ == '__main__':
    try:
        print_even_numbers()
    except ValueError as e:
        print(e)