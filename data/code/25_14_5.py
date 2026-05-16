def even_zero_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            if num == 0:
                yield True
if __name__ == '__main__':
    print(list(even_zero_generator(0, 10)))
    print(list(even_zero_generator(1, 5)))
    print(list(even_zero_generator(2, 2)))
    print(list(even_zero_generator(10, 10)))