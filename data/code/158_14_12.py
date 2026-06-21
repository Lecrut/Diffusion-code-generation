def get_even_numbers():
    even_numbers = [i for i in range(100) if (i & 1) == 0]
    return sorted(even_numbers)

if __name__ == '__main__':
    sample_values = [4, 7, 0, -3, "hello", 12.5]
    even_nums = get_even_numbers()
    print([num for num in even_nums if num in range(0, 100)])