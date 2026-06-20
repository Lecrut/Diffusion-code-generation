def sum_range(start: int, end: int) -> int:
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end values must be integers.")
    if start > end:
        raise ValueError("Start value must be less than or equal to end value.")
    return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    result = sum_range(1, 10)
    print(f"The sum of numbers from 1 to 10 is: {result}")