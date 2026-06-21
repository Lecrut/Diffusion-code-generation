def filter_even_numbers():
    return [num for num in range(100) if not (num & 1)]

if __name__ == '__main__':
    print(filter_even_numbers())