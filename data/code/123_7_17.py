def sum_even_numbers(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end values must be integers.")
    if start > end:
        raise ValueError("Start value must be less than or equal to end value.")
    
    return sum(x for x in range(start, end + 1) if x % 2 == 0)

if __name__ == '__main__':
    print(sum_even_numbers(1, 10))