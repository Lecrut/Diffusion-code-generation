def count_evens(a, b):
    lower = min(a, b)
    upper = max(a, b)
    if lower > upper:
        return 0
    first_even = lower if lower % 2 == 0 else lower + 1
    last_even = upper if upper % 2 == 0 else upper - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    a = 1
    b = 10
    print(count_evens(a, b))
    a = 5
    b = 5
    print(count_evens(a, b))
    a = 6
    b = 6
    print(count_evens(a, b))
    a = -5
    b = 5
    print(count_evens(a, b))