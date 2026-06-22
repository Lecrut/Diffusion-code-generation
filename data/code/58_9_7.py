def count_even(start: int, stop: int) -> int:
    if start > stop:
        return 0
    effective_start = start if start % 2 == 0 else start + 1
    effective_stop = stop if stop % 2 == 0 else stop - 1
    if effective_start > effective_stop:
        return 0
    return (effective_stop - effective_start) // 2 + 1

if __name__ == '__main__':
    result = count_even(1, 10)
    print(result)