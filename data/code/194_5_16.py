def longest_string_generator(iterable):
    max_length = 0
    longest_string = None
    for item in iterable:
        if len(item) > max_length:
            max_length = len(item)
            longest_string = item
        yield longest_string
if __name__ == '__main__':
    sample_iterable = ['apple', 'banana', 'programming', 'algorithm', 'supercalifragilisticexpialidocious']
    generator = longest_string_generator(sample_iterable)
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))