def count_even_between(low, high):
    if low > high:
        low, high = high, low
    if low % 2 != 0:
        low += 1
    if high % 2 != 0:
        high -= 1
    if low > high:
        return 0
    return (high - low) // 2 + 1

if __name__ == '__main__':
    result = count_even_between(3, 10)
    print(result)