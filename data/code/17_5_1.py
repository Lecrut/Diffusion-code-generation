def last_item(seq):
    return seq[-1]

if __name__ == '__main__':
    items = {'a': 1, 'b': 2, 'c': 3}
    sample_sequence = list(items.values())
    print(last_item(sample_sequence))