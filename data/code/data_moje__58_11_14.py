def count_even_integers(start, end):
    if start > end:
        return 0
    lower = start if start % 2 == 0 else start + 1
    upper = end if end % 2 == 0 else end - 1
    if lower > upper:
        return 0
    return (upper - lower) // 2 + 1

if __name__ == '__main__':
    result = count_even_integers(1, 10)
    print(result)