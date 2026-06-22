def generate_mult_table(n, start, end):
    if not isinstance(n, int) or not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("All arguments must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return [f"{n} x {i} = {n * i}" for i in range(start, end + 1)]

if __name__ == '__main__':
    print('\n'.join(generate_mult_table(5, 1, 10)))