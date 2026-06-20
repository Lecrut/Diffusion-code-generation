def sum_even_numbers(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers.")
    if start > end:
        raise ValueError("Start must be less than or equal to end.")
    return sum(x for x in range(start, end + 1) if x % 2 == 0)

if __name__ == '__main__':
    result = sum_even_numbers(1, 10)
    print(result)