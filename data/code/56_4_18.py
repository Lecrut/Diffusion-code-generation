def get_multiplication_table(number: int, start: int = 1, end: int = 10):
    if not isinstance(number, int) or not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Inputs must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return [f"{number} x {i} = {number * i}" for i in range(start, end + 1)]

if __name__ == '__main__':
    result = get_multiplication_table(5, 1, 10)
    print('\n'.join(result))