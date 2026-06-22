def get_from_generator(gen, index):
    iterator = iter(gen)
    result = None
    for i in range(index + 1):
        result = next(iterator)
    return result

if __name__ == '__main__':
    gen = (x ** 2 for x in range(10))
    value = get_from_generator(gen, 4)
    print(value)