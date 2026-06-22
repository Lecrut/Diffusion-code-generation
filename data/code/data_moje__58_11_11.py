def count_evens(low, high):
    if low > high:
        low, high = (high, low)
    first_even = low if low % 2 == 0 else low + 1
    last_even = high if high % 2 == 0 else high - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1
if __name__ == '__main__':
    print(count_evens(1, 10))
    print(count_evens(2, 2))
    print(count_evens(5, 5))
    print(count_evens(1, 1))
    print(count_evens(10, 20))