import itertools

def extract_even_numbers(start, end):
    if not (isinstance(start, int) and isinstance(end, int)):
        raise ValueError("Start and end must be integers")
    if start >= end:
        raise ValueError("End must be greater than start")
    
    numbers = range(start, end + 1)
    even_numbers = list(itertools.islice(numbers, 0, None, 2))
    return even_numbers

if __name__ == '__main__':
    try:
        sample_range_1 = extract_even_numbers(1, 30)
        print(f"Range: 1 to 30, Even numbers: {sample_range_1}")
        
        sample_range_2 = extract_even_numbers(5, 15)
        print(f"Range: 5 to 15, Even numbers: {sample_range_2}")
        
        sample_range_3 = extract_even_numbers(20, 40)
        print(f"Range: 20 to 40, Even numbers: {sample_range_3}")
    except ValueError as e:
        print(e)