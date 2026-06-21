def get_first(generator):
    return next(generator)

if __name__ == '__main__':
    sample_gen = (x * 2 for x in range(5))
    result = get_first(sample_gen)
    print(result)