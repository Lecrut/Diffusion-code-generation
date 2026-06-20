def invert_boolean_values(iterable):
    for value in iterable:
        yield not value

if __name__ == '__main__':
    sample_values = [False, True, False]
    inverted_results = list(invert_boolean_values(sample_values))
    print(inverted_results)