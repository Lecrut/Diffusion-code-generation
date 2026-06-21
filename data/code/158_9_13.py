odd_numbers = {1, 3, 5, 7, 9, 11, 13, 15}

def find_even_numbers():
    return set(range(1, 16)) - odd_numbers

if __name__ == '__main__':
    even_numbers = find_even_numbers()
    print(even_numbers)