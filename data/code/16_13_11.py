def get_first_element(generator):
    try:
        return next(generator)
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_generator = (x for x in range(5))
    result = get_first_element(sample_generator)
    print(result)