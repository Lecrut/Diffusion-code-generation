def get_even_numbers():
    return [n for n in range(0, 100) if n & 1 == 0]

if __name__ == '__main__':
    print(get_even_numbers())