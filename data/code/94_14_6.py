def any_truthy(seq):
    return any(item for item in seq)

if __name__ == '__main__':
    sample_values = [0, '', [], {}, None, False]
    print(any_truthy(sample_values))