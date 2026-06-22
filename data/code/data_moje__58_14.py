def count_even_numbers(a, b):
    lower = min(a, b)
    upper = max(a, b)
    first_even = lower if lower % 2 == 0 else lower + 1
    last_even = upper if upper % 2 == 0 else upper - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))