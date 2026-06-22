def count_even_between(a, b):
    if a > b:
        a, b = b, a
    start = 0 if a % 2 == 0 else a + 1
    end = b if b % 2 == 0 else b - 1
    if start > end:
        return 0
    return (end - start) // 2 + 1

if __name__ == '__main__':
    lower = 10
    upper = 30
    result = count_even_between(lower, upper)
    print(result)