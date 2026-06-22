def count_even_between(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    
    lower = start if start % 2 == 0 else start + 1
    upper = end if end % 2 == 0 else end - 1
    
    if lower > upper:
        return 0
    
    return (upper - lower) // 2 + 1

if __name__ == '__main__':
    print(count_even_between(1, 10))
    print(count_even_between(2, 8))
    print(count_even_between(10, 1))
    print(count_even_between(3, 3))