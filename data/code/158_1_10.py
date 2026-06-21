def is_valid_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers.")
    if start > end:
        raise ValueError("Start must be less than or equal to end.")

def get_even_numbers(start, end):
    is_valid_range(start, end)
    return list(range(start, end + 1))[::2]

if __name__ == '__main__':
    even_numbers = get_even_numbers(1, 10)
    print(even_numbers)