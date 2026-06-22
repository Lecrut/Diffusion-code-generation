def compare_lengths(seq1, seq2):
    len1 = iter(len(chunk) for chunk in seq1)
    len2 = iter(len(chunk) for chunk in seq2)

    while True:
        try:
            l1 = next(len1)
        except StopIteration:
            l1 = None

        try:
            l2 = next(len2)
        except StopIteration:
            l2 = None

        if l1 is None and l2 is None:
            break
        elif l1 is None:
            yield -1
        elif l2 is None:
            yield 1
        else:
            yield (l1 > l2) - (l1 < l2)

if __name__ == '__main__':
    seq1 = ['hello', 'world']
    seq2 = ['hi', 'there']

    for result in compare_lengths(seq1, seq2):
        print(result)