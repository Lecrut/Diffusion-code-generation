import itertools

def extract_even_numbers(range_start, range_end):
    if not (isinstance(range_start, int) and isinstance(range_end, int)):
        raise ValueError("Both range_start and range_end must be integers.")
    if range_start > range_end:
        raise ValueError("range_start must be less than or equal to range_end.")

    even_numbers = list(itertools.islice(range(range_start, range_end + 1), None, 2))
    return even_numbers

if __name__ == '__main__':
    sample_range_start = 1
    sample_range_end = 30
    try:
        result = extract_even_numbers(sample_range_start, sample_range_end)
        print(f"Even numbers between {sample_range_start} and {sample_range_end}: {result}")
    except ValueError as e:
        print(e)