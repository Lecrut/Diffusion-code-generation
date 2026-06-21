if __name__ == '__main__':
    max_value = 50
    even_numbers_generator = [x for x in range(1, max_value + 1) if x % 2 == 0]
    print(even_numbers_generator)