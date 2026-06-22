def count_evens(start: int, stop: int) -> int:
    if start > stop:
        return 0
    if start % 2 == 0:
        first_even = start
    else:
        first_even = start + 1
    
    if first_even > stop:
        return 0
    
    count = (stop - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    start = 3
    stop = 10
    result = count_evens(start, stop)
    print(result)