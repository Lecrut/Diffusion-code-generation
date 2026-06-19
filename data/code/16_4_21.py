def positive_filter(iterable):
    for number in iterable:
        if number > 0:
            yield True

if __name__ == '__main__':
    sample_values = [-10, -1, 0, 5, 9, -3, 7]
    result = list(positive_filter(sample_values))
    print(result)