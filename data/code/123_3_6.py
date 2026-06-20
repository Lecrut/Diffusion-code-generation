def sum_range(start, end):
    return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    sample_start = 5
    sample_end = 10
    result = sum_range(sample_start, sample_end)
    print(f"The sum of numbers from {sample_start} to {sample_end} is: {result}")