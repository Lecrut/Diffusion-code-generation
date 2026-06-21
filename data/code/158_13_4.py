def print_even_numbers(start=1, end=20, step=2):
    if not (isinstance(start, int) and isinstance(end, int) and isinstance(step, int)):
        raise ValueError("All parameters must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    if step <= 0:
        raise ValueError("Step must be greater than zero")

    for num in range(start, end + 1, step):
        print(num)

if __name__ == '__main__':
    print_even_numbers()