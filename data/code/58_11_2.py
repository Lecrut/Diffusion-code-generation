def count_even_numbers(low, high):
    if low > high:
        return 0
    count_high = high // 2
    count_low = (low - 1) // 2
    return count_high - count_low
if __name__ == '__main__':
    sample_low = 1
    sample_high = 10
    result = count_even_numbers(sample_low, sample_high)
    print(result)