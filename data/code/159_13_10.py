if __name__ == '__main__':
    sample_tuple = (10, 23, 45, 68, 90, 113)
    odd_numbers = tuple(x for x in sample_tuple if x % 2 != 0)
    print(odd_numbers)