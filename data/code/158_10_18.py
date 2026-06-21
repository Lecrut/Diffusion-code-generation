def list_even_numbers(start=0, end=50):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end values must be integers.")
    if start < 0 or end > 50:
        raise ValueError("Start must be between 0 and 50, inclusive. End must be less than or equal to 50.")
    
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers

if __name__ == '__main__':
    result = list_even_numbers()
    print(result)