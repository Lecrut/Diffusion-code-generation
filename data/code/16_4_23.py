def positive_filter(iterable):
    for number in iterable:
        if number > 0:
            yield True

if __name__ == '__main__':
    sample_values = [-10, -5, 0, 3, 7, -2, 8]
    result = list(positive_filter(sample_values))
    print(result)