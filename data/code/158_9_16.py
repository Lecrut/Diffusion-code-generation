ODD_NUMBERS = {1, 3, 5, 7, 9, 11, 13, 15}

def find_even_numbers(odd_set):
    all_numbers = set(range(1, 16))
    even_numbers = all_numbers - odd_set
    return even_numbers

if __name__ == '__main__':
    even_numbers = find_even_numbers(ODD_NUMBERS)
    print(even_numbers)