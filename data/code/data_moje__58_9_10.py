def count_even_numbers(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    
    start_inclusive = start if start % 2 == 0 else start + 1
    end_inclusive = end if end % 2 == 0 else end - 1
    
    if start_inclusive > end_inclusive:
        return 0
    
    count = (end_inclusive - start_inclusive) // 2 + 1
    return count

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)