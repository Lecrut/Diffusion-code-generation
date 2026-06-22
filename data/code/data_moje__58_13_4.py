def count_even_numbers(start, end):
    if start > end:
        return 0

    def first_even(n):
        if n % 2 == 0:
            return n
        return n + 1

    def last_even(n):
        if n % 2 == 0:
            return n
        return n - 1
    first = first_even(start)
    last = last_even(end)
    if first > last:
        return 0
    return (last - first) // 2 + 1
if __name__ == '__main__':
    result1 = count_even_numbers(1, 10)
    print(result1)
    result2 = count_even_numbers(5, 5)
    print(result2)
    result3 = count_even_numbers(10, 1)
    print(result3)
    result4 = count_even_numbers(2, 2)
    print(result4)
    result5 = count_even_numbers(-5, 5)
    print(result5)