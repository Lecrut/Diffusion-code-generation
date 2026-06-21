import itertools

def extract_even_numbers(start, end):
    range_obj = range(start, end + 1)
    even_numbers = list(itertools.islice(range_obj, 0, None, 2))
    return even_numbers

if __name__ == '__main__':
    sample_range_start = 1
    sample_range_end = 30
    result = extract_even_numbers(sample_range_start, sample_range_end)
    print(f"Range {sample_range_start}-{sample_range_end}: Even numbers: {result}")