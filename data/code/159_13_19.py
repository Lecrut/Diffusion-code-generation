if __name__ == '__main__':
    sample_tuple = (12, 27, 34, 49, 58, 67)
    odd_numbers = tuple(x for x in sample_tuple if x % 2 != 0)
    print(odd_numbers)