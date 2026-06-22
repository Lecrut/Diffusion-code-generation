def positive_filter(iterable):
    for number in iterable:
        if number > 0:
            yield True

if __name__ == '__main__':
    sample_values = [-1, 2, -3, 4, 5]
    result = list(positive_filter(sample_values))
    print(result)