if __name__ == '__main__':
    odd_numbers = tuple(x for x in (1, 2, 3, 4, 5, 6, 7, 8, 9) if x % 2 != 0)
    print(odd_numbers)