import itertools

def extract_even_numbers(start, end):
    return list(itertools.islice(range(start, end + 1), None, 2))

if __name__ == '__main__':
    sample_range = range(1, 31)
    result = extract_even_numbers(*sample_range)
    print(f"Range: {sample_range}")
    print(f"Even numbers: {result}")