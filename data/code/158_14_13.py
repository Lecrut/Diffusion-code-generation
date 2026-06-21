def filter_even_numbers():
    return [num for num in range(100) if (num & 1) == 0]

if __name__ == '__main__':
    even_numbers = filter_even_numbers()
    print(even_numbers)