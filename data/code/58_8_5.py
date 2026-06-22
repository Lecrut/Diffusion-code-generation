def count_even_numbers(a, b):
    start = min(a, b)
    end = max(a, b)
    first_even = start + (start % 2)
    last_even = end - (end % 2)
    if first_even > last_even:
        return 0
    return (last_even - first_even) // 2 + 1

if __name__ == '__main__':
    a = 1
    b = 10
    result = count_even_numbers(a, b)
    print(result)