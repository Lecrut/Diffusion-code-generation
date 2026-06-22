def get_first_element(generator):
    try:
        return next(generator)
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_gen = (x * 2 for x in range(5))
    first = get_first_element(sample_gen)
    print(first)
    sample_empty = (x for x in [])
    first_empty = get_first_element(sample_empty)
    print(first_empty)