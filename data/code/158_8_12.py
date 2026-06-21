import itertools

def extract_even_numbers(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end must be integers")
    if start < 1 or end > 30:
        raise ValueError("Range must be between 1 and 30 inclusive")
    
    range_obj = range(start, end + 1)
    even_numbers = list(itertools.islice(range_obj, 0, None, 2))
    return even_numbers

if __name__ == '__main__':
    sample_range_1 = (1, 30)
    result_1 = extract_even_numbers(*sample_range_1)
    print(f"Range: {sample_range_1}, Even numbers: {result_1}")