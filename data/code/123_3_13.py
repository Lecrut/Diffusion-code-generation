def sum_range(start, end):
    return (end - start + 1) * (start + end) // 2

if __name__ == '__main__':
    START = 1
    END = 10
    result = sum_range(START, END)
    print(f"The sum of numbers from {START} to {END} is: {result}")