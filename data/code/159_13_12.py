if __name__ == '__main__':
    numbers = (12, 15, 18, 21, 24, 27)
    odd_numbers = tuple(x for x in numbers if x % 2 != 0)
    print(odd_numbers)