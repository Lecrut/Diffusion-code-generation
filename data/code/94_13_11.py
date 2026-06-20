def any_truthy(iterable):
    return any(item for item in iterable)

if __name__ == '__main__':
    sample_values = [0, '', None, False, 42]
    print(any_truthy(sample_values))