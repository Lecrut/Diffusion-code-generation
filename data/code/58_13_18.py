def count_even_in_range(start: int, stop: int) -> int:
    if start > stop:
        return 0
    effective_stop = stop if stop % 2 == 0 else stop - 1
    effective_start = start if start % 2 == 0 else start + 1
    if effective_start > effective_stop:
        return 0
    count = (effective_stop - effective_start) // 2 + 1
    return count

if __name__ == '__main__':
    result = count_even_in_range(1, 10)
    print(result)