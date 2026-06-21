def positive_filter(iterable):
    for item in iterable:
        if item > 0:
            yield True

if __name__ == '__main__':
    sample_values = [-1, 2, -3, 4, 0, -5, 6]
    result = list(positive_filter(sample_values))
    print(result)