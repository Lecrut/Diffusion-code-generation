def count_even_numbers(start: int, stop: int) -> int:
    if start > stop:
        start, stop = stop, start
    
    first_even = start if start % 2 == 0 else start + 1
    last_even = stop if stop % 2 == 0 else stop - 1
    
    if first_even > last_even:
        return 0
    
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(3, 10)
    print(result)