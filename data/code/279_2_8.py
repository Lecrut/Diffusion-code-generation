def print_even_numbers(start=100, end=200):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end values must be integers.")
    if start >= end:
        raise ValueError("Start value must be less than end value.")

    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

if __name__ == '__main__':
    try:
        print_even_numbers()
    except Exception as e:
        print(e)