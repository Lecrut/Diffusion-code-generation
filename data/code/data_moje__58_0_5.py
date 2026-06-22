def count_evens(start: int, end: int) -> int:
    if start > end:
        return 0
    first_even = start + (start % 2)
    if first_even > end:
        return 0
    last_even = end - (end % 2)
    if last_even < first_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_evens(2, 10)
    print(result)