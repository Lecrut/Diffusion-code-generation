if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5, 6, 7)
    odd_numbers = tuple(x for x in sample_tuple if x % 2 != 0)
    print(odd_numbers)