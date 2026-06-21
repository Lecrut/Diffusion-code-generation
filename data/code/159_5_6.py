if __name__ == '__main__':
    sample_sequence = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    odd_numbers = tuple(x for x in sample_sequence if x % 2 != 0)
    print(odd_numbers)