def even_and_zero_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            if num == 0:
                yield True
if __name__ == '__main__':
    generator = even_and_zero_generator(0, 10)
    results = list(generator)
    print(results)