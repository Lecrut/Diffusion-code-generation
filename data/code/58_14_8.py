def count_even(start: int, end: int) -> int:
    lower = min(start, end)
    upper = max(start, end)
    if lower % 2 != 0:
        lower += 1
    if upper % 2 != 0:
        upper -= 1
    if lower > upper:
        return 0
    return (upper - lower) // 2 + 1

if __name__ == '__main__':
    result = count_even(1, 10)
    print(result)