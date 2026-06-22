def count_even(a, b):
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
    start_val = 10
    end_val = 20
    result = count_even(start_val, end_val)
    print(result)