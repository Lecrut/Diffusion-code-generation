def count_evens_between(a, b):
    low = min(a, b)
    high = max(a, b)
    if low % 2 != 0:
        low += 1
    if high % 2 != 0:
        high -= 1
    if low > high:
        return 0
    return (high - low) // 2 + 1

if __name__ == '__main__':
    start = 3
    end = 15
    result = count_evens_between(start, end)
    print(result)