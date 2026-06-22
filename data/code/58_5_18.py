def count_even_numbers(start: int, end: int) -> int:
    if start > end:
        return 0
    effective_end = end
    effective_start = start
    
    if effective_start % 2 != 0:
        effective_start += 1
    if effective_end % 2 != 0:
        effective_end -= 1
        
    if effective_start > effective_end:
        return 0
        
    return (effective_end - effective_start) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)