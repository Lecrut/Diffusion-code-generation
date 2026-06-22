def count_evens(start: int, end: int) -> int:
    if start > end:
        raise ValueError("start must be less than or equal to end")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")

    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    
    if first_even > last_even:
        return 0
    
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    start = 1
    end = 10
    result = count_evens(start, end)
    print(result)