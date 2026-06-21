def find_even_numbers():
    return [n for n in range(0, 100) if not (n & 1)]

if __name__ == '__main__':
    print(find_even_numbers())