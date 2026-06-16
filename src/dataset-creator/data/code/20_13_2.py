def filter_non_positive(iterable):
    return [x for x in iterable if not (isinstance(x, int) and x <= 0)]
if __name__ == '__main__':
    sample_data = [-5, -1, 3.7, 42, 0, "text", True]
    result = filter_non_positive(sample_data)
    print(result)