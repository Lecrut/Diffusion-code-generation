if __name__ == '__main__':
    SAMPLE_TUPLE = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    odd_numbers = tuple(x for x in SAMPLE_TUPLE if x % 2 != 0)
    print(odd_numbers)