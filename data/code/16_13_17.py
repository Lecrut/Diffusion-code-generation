def get_first_element(generator):
    try:
        return next(generator)
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_generator = (x for x in range(1, 10))
    result = get_first_element(sample_generator)
    print(result)
    another_generator = iter([])
    empty_result = get_first_element(another_generator)
    print(empty_result)