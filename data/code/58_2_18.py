def count_even_numbers(start: int, end: int) -> int:
    if start > end:
        return 0
    
    low = start if start % 2 == 0 else start + 1
    high = end if end % 2 == 0 else end - 1
    
    if low > high:
        return 0
    
    count = (high - low) >> 1
    return count + 1

if __name__ == '__main__':
    start_val = 3
    end_val = 10
    result = count_even_numbers(start_val, end_val)
    print(result)