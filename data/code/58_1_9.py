def count_even_numbers(a, b):
    lower = min(a, b)
    upper = max(a, b)
    if lower % 2 != 0:
        lower += 1
    if upper % 2 != 0:
        upper -= 1
    if lower > upper:
        return 0
    return (upper - lower) // 2 + 1

if __name__ == '__main__':
    a = 3
    b = 10
    result = count_even_numbers(a, b)
    print(result)