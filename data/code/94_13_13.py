def contains_truthy(iterable):
    return any(iterable)

if __name__ == '__main__':
    sample_values = [0, False, None, [], {}, (), 'hello']
    result = contains_truthy(sample_values)
    print(result)