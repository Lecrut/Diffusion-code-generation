def get_first(generator):
    iterator = iter(generator)
    return next(iterator)

if __name__ == '__main__':
    sample_generator = (x for x in range(100))
    result = get_first(sample_generator)
    print(result)