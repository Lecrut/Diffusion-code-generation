def is_valid_range(start, end):
    return isinstance(start, int) and isinstance(end, int) and start <= end

def sum_even_numbers(start, end):
    if not is_valid_range(start, end):
        raise ValueError("Invalid range")
    
    return sum(x for x in range(start, end + 1) if x % 2 == 0)

if __name__ == '__main__':
    result = sum_even_numbers(1, 10)
    print(result)