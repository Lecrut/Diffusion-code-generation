def even_numbers_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
if __name__ == '__main__':
    limit = 20
    generator = even_numbers_generator(limit)
    result = list(generator)
    print(result)