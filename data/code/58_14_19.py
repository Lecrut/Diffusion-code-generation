def count_even_numbers(a, b):
    low = min(a, b)
    high = max(a, b)
    first_even = low + (low % 2)
    if first_even > high:
        return 0
    last_even = high - (high % 2)
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)