def _validate_bounds(low: int, high: int) -> tuple[int, int]:
    if low > high:
        lower = high
        upper = low
    else:
        lower = low
        upper = high
    return lower, upper

def count_even_numbers(low: int, high: int) -> int:
    lower, upper = _validate_bounds(low, high)
    if lower > upper:
        return 0
    first_even = lower if lower % 2 == 0 else lower + 1
    if first_even > upper:
        return 0
    last_even = upper if upper % 2 == 0 else upper - 1
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    sample_low = 5
    sample_high = 15
    result = count_even_numbers(sample_low, sample_high)
    print(result)