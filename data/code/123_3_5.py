def validate_range(start, end):
    if start > end:
        raise ValueError("Start must be less than or equal to end")

def sum_range(start, end):
    validate_range(start, end)
    return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    try:
        result = sum_range(1, 10)
        print(result)
    except ValueError as e:
        print(e)