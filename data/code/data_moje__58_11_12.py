def count_evens_in_range(low, high):
    if low > high:
        low, high = (high, low)
    if low % 2 == 0:
        first_even = low
    else:
        first_even = low + 1
    if high % 2 == 0:
        last_even = high
    else:
        last_even = high - 1
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1
if __name__ == '__main__':
    sample_low = 3
    sample_high = 15
    result = count_evens_in_range(sample_low, sample_high)
    print(result)