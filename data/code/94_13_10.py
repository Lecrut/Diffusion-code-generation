def any_truthy(iterable):
    return any((item for item in iterable))
if __name__ == '__main__':
    sample_values = [0, False, None, '', [], {}, (), set()]
    print(any_truthy(sample_values))
    sample_values = [0, False, None, '', 'hello', [1], {2}, (3,), {4}]
    print(any_truthy(sample_values))