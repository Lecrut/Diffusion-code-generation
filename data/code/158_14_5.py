def find_even_numbers():
    return [i for i in range(0, 100) if (i & 1) == 0]

if __name__ == '__main__':
    print(find_even_numbers())