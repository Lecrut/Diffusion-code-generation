def count_evens(start: int, end: int) -> int:
    if start > end:
        return 0
    even_start = start if start % 2 == 0 else start + 1
    even_end = end if end % 2 == 0 else end - 1
    if even_start > even_end:
        return 0
    return (even_end - even_start) // 2 + 1

if __name__ == '__main__':
    result = count_evens(2, 10)
    print(result)