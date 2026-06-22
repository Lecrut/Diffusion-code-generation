def count_evens(start: int, stop: int) -> int:
    if start > stop:
        return 0
    
    total_numbers = stop - start + 1
    
    if total_numbers <= 0:
        return 0
    
    if start % 2 == 0:
        first_is_even = True
    else:
        first_is_even = False
    
    if first_is_even:
        return (total_numbers + 1) // 2
    else:
        return total_numbers // 2

if __name__ == '__main__':
    start = 2
    stop = 10
    result = count_evens(start, stop)
    print(result)