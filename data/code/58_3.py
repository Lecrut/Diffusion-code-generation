def count_even_in_interval(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    
    if first_even > last_even:
        return 0
    
    count = (last_even - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    result = count_even_in_interval(2, 10)
    print(result)
    
    result2 = count_even_in_interval(3, 9)
    print(result2)
    
    result3 = count_even_in_interval(1, 1)
    print(result3)