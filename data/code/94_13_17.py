def contains_truthy(iterable):
    return any(item for item in iterable)

if __name__ == '__main__':
    sample_values = [0, False, None, [], (), {}, set(), '']
    print(contains_truthy(sample_values))