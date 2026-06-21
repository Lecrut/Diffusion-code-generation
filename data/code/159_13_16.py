if __name__ == '__main__':
    numbers = (12, 34, 56, 78, 90, 112, 133)
    odd_numbers = tuple(x for x in numbers if x % 2 != 0)
    print(odd_numbers)