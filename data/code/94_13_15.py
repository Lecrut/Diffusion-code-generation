def any_truthy(iterable):
    return any(item for item in iterable)

if __name__ == '__main__':
    sample_values = [0, False, None, [], {}, (), ""]
    print(any_truthy(sample_values))