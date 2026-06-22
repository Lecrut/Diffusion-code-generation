def first_element_generator(iterable):
    return (item for item in iterable).send(None)

if __name__ == '__main__':
    sample_iterable = [42, 84, 126, 168, 210]
    generator = first_element_generator(sample_iterable)
    print(next(generator))