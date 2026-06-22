def count_evens(start, end):
    if start > end:
        return 0
    def count_non_negative_even(n):
        if n < 0:
            return 0
        return n // 2 + 1
    def count_negative_even(n):
        return (n + 1) // 2
    def count_even_upto(n):
        if n >= 0:
            return count_non_negative_even(n)
        return count_negative_even(n)
    result = count_even_upto(end) - count_even_upto(start - 1)
    return result

if __name__ == '__main__':
    test_cases = [
        (1, 10),
        (2, 2),
        (3, 3),
        (4, 100),
        (10, 5),
        (-10, 10),
        (-5, -1),
        (0, 5),
        (-2, -2)
    ]
    for s, e in test_cases:
        print(count_evens(s, e))