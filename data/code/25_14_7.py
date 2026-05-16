def even_zero_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            if number == 0:
                yield True
if __name__ == '__main__':
    print(list(even_zero_generator(0, 10)))
    print(list(even_zero_generator(2, 8)))
    print(list(even_zero_generator(1, 1)))
    print(list(even_zero_generator(10, 10)))