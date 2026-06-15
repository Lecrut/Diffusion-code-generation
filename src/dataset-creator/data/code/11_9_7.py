def multiply_consecutive(limit):
    for i in range(1, limit + 1):
        yield i * (i + 1)
if __name__ == '__main__':
    limit = 5
    generator = multiply_consecutive(limit)
    results = list(generator)
    print(results)