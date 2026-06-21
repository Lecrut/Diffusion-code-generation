def is_positive(number):
    return number > 0

def positive_filter(iterable):
    for item in iterable:
        if is_positive(item):
            yield True

if __name__ == '__main__':
    sample_values = [-20, -15, 0, 15, 20]
    result = list(positive_filter(sample_values))
    print(result)