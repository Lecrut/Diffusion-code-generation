def count_even_numbers(a, b):
    a, b = min(a, b), max(a, b)
    return (b // 2) - ((a - 1) // 2)

if __name__ == '__main__':
    print(count_even_numbers(1, 10))