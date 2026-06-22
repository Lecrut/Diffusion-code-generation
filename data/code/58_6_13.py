def count_even_numbers(min_val, max_val):
    if min_val > max_val:
        return 0
    if min_val % 2 == 0:
        return (max_val - min_val) // 2 + 1
    else:
        return (max_val - min_val) // 2

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 10))
    print(count_even_numbers(5, 5))
    print(count_even_numbers(10, 10))
    print(count_even_numbers(1, 1))