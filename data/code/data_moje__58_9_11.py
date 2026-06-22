def count_even_numbers(start, end):
    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        raise TypeError("Start and end must be numeric")
    if start > end:
        start, end = end, start
    start = int(start)
    end = int(end)
    if start == 0:
        first_even = 0
    else:
        first_even = start + (start % 2)
    if end == 0:
        last_even = 0
    else:
        last_even = end - (end % 2)
    if first_even > last_even:
        return 0
    count = (last_even - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(5, 15))
    print(count_even_numbers(0, 0))
    print(count_even_numbers(-5, 5))
    print(count_even_numbers(2, 2))