def count_even_numbers(a, b):
    lower = min(a, b)
    upper = max(a, b)
    if lower > upper:
        return 0
    first_even = lower + (lower % 2 != 0)
    last_even = upper - (upper % 2 != 0)
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)