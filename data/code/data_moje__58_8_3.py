def count_even_numbers(a, b):
    start = min(a, b)
    end = max(a, b)
    if start % 2 == 0:
        lower = start
    else:
        lower = start + 1
    if end % 2 == 0:
        upper = end
    else:
        upper = end - 1
    if lower > upper:
        return 0
    return (upper - lower) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(3, 10)
    print(result)