def sum_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    try:
        result = sum_range(1, 10)
        print(f"The sum of numbers from 1 to 10 is: {result}")
    except ValueError as e:
        print(e)