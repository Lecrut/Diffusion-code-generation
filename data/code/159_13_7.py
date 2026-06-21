if __name__ == '__main__':
    source_tuple = (12, 34, 56, 78, 90, 111)
    odd_numbers = tuple(x for x in source_tuple if x % 2 != 0)
    print(odd_numbers)