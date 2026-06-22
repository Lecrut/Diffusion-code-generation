def count_even_between(lower: int, upper: int) -> int:
    if lower > upper:
        lower, upper = upper, lower
    if lower % 2 != 0:
        lower += 1
    if upper % 2 != 0:
        upper -= 1
    if lower > upper:
        return 0
    return (upper - lower) // 2 + 1

if __name__ == '__main__':
    print(count_even_between(1, 10))
    print(count_even_between(2, 20))
    print(count_even_between(-5, 5))
    print(count_even_between(10, 2))