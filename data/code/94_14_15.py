def any_truthy(sequence):
    return any(item for item in sequence)

if __name__ == '__main__':
    sample_sequence = [0, False, None, [], {}, (), ""]
    print(any_truthy(sample_sequence))