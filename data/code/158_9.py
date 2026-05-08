if __name__ == '__main__':
    data = list(range(1, 1000000))
    even_numbers = [x for x in data if x % 2 == 0]
    print(even_numbers)