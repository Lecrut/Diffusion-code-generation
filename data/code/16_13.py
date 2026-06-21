def get_first_element(generator):
    return next(generator)

if __name__ == '__main__':
    sample_generator = (x for x in [10, 20, 30])
    result = get_first_element(sample_generator)
    print(result)