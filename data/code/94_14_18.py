def any_truthy(seq):
    return any(seq)

if __name__ == '__main__':
    sample_values = [0, False, None, '', [], {}, set()]
    print(any_truthy(sample_values))