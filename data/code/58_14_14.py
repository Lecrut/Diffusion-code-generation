def count_even_numbers(a, b):
    low = min(a, b)
    high = max(a, b)
    first_even = low + (low % 2 != 0)
    if first_even > high:
        return 0
    return (high - first_even) // 2 + 1

if __name__ == '__main__':
    start = 1
    end = 10
    print(count_even_numbers(start, end))