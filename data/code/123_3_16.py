def sum_range(start, end):
    if not (isinstance(start, int) and isinstance(end, int)):
        raise ValueError("Both start and end must be integers.")
    if start > end:
        raise ValueError("Start must be less than or equal to end.")
    
    return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    start_val = 3
    end_val = 9
    result = sum_range(start_val, end_val)
    print(f"The sum of numbers from {start_val} to {end_val} is: {result}")