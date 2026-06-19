def compare_lengths(seq1, seq2):
    len1 = iter(len(chunk) for chunk in seq1)
    len2 = iter(len(chunk) for chunk in seq2)

    while True:
        try:
            l1 = next(len1)
        except StopIteration:
            if next(len2, None) is not None:
                yield False
            break

        try:
            l2 = next(len2)
        except StopIteration:
            yield False
            continue

        yield l1 == l2

if __name__ == '__main__':
    seq1 = ['hello', 'world']
    seq2 = ['hello', 'world']

    for result in compare_lengths(seq1, seq2):
        print(result)