def is_valid_range(start, end):
    return isinstance(start, int) and isinstance(end, int) and start <= end

def get_even_numbers(start, end):
    if not is_valid_range(start, end):
        raise ValueError("Invalid range: Start must be less than or equal to End")
    
    return list(range(start, end + 1))[::2]

if __name__ == '__main__':
    even_numbers = get_even_numbers(1, 10)
    print(even_numbers)