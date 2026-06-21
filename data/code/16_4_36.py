def positive_filter(iterable):
    for item in iterable:
        if item > 0:
            yield True

if __name__ == '__main__':
    sample_values = [-15, -3, 0, 2, 6, -1, 4]
    result = list(positive_filter(sample_values))
    print(result)