odd_numbers = {1, 3, 5, 7, 9, 11, 13, 15}
all_integers = set(range(1, 16))
even_numbers = all_integers - odd_numbers

if __name__ == '__main__':
    print(even_numbers)