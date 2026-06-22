def count_even(start: int, end: int) -> int:
    lower = min(start, end)
    upper = max(start, end)
    first_even = lower if lower % 2 == 0 else lower + 1
    last_even = upper if upper % 2 == 0 else upper - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    start_val = 10
    end_val = 20
    result = count_even(start_val, end_val)
    print(result)