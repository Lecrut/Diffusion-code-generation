def find_even_numbers():
    even_numbers = [i for i in range(0, 100) if (i & 1) == 0]
    return sorted(even_numbers)

if __name__ == '__main__':
    print(find_even_numbers())