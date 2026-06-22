def count_evens(start: int, stop: int) -> int:
    lower = max(start, stop if start > stop else start)
    upper = min(start, stop)
    
    first_even = lower + (lower % 2 != 0)
    if first_even > upper:
        return 0
    
    last_even = upper - (upper % 2 != 0)
    
    count = (last_even - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    result = count_evens(2, 10)
    print(result)