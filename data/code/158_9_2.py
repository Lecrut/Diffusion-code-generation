odd_numbers = {1, 3, 5, 7, 9, 11, 13, 15}

def find_even_numbers():
    all_numbers = set(range(1, 16))
    even_numbers = all_numbers - odd_numbers
    return even_numbers

if __name__ == '__main__':
    print(find_even_numbers())