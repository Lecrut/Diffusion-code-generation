def count_even_numbers(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    
    count = (end - start) // 2 + 1
    
    if start % 2 != 0 and end % 2 != 0:
        count -= 1
        
    return count

if __name__ == '__main__':
    print(count_even_numbers(2, 10))
    print(count_even_numbers(1, 10))
    print(count_even_numbers(1, 5))
    print(count_even_numbers(4, 4))
    print(count_even_numbers(5, 5))
    print(count_even_numbers(1, 1))
    print(count_even_numbers(2, 2))