def count_even(start: int, stop: int) -> int:
    if start > stop:
        start, stop = stop, start
    
    if start % 2 == 0:
        first_even = start
    else:
        first_even = start + 1
        
    if stop % 2 == 0:
        last_even = stop
    else:
        last_even = stop - 1
        
    if first_even > last_even:
        return 0
        
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even(1, 10)
    print(result)