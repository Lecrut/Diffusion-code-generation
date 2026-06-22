def get_first_element(iterator):
    try:
        return next(iterator)
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_generator = (x * 2 for x in range(1, 10))
    result = get_first_element(sample_generator)
    print(result)