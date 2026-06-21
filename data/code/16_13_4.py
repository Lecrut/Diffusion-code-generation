def get_first_element(generator):
    return next(generator)

if __name__ == '__main__':
    sample_generator = (x * 2 for x in range(10))
    result = get_first_element(sample_generator)
    print(result)