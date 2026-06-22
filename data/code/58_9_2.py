def count_even_numbers(start, end):
    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        raise TypeError("Start and end must be numeric types")
    if isinstance(start, float) and start != int(start):
        start = int(start)
    if isinstance(end, float) and end != int(end):
        end = int(end)
    if start > end:
        return 0
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 10))
    print(count_even_numbers(3, 3))
    print(count_even_numbers(10, 1))
    print(count_even_numbers(0, 0))