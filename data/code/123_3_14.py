def sum_range(start, end):
    return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    start_val = 10
    end_val = 30
    result = sum_range(start_val, end_val)
    print(f"The sum of numbers from {start_val} to {end_val} is: {result}")