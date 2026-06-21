def get_even_numbers(start, end):
    if not (isinstance(start, int) and isinstance(end, int)):
        raise ValueError("Both start and end must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")

    return list(range(start, end + 1))[::2]

if __name__ == '__main__':
    print(get_even_numbers(1, 10))