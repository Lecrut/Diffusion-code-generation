MAX_VALUE = 50

if __name__ == '__main__':
    even_numbers = [x for x in range(1, MAX_VALUE + 1) if x % 2 == 0]
    print(even_numbers)