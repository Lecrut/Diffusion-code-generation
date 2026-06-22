def compare_lengths(seq1, seq2):
    len1 = iter((len(chunk) for chunk in seq1))
    len2 = iter((len(chunk) for chunk in seq2))
    while True:
        try:
            l1 = next(len1)
            l2 = next(len2)
            yield (l1, l2)
        except StopIteration:
            break
if __name__ == '__main__':

    def sample_generator(n):
        for i in range(n):
            yield ([i] * 1000)
    seq1 = sample_generator(5)
    seq2 = sample_generator(3)
    for length_pair in compare_lengths(seq1, seq2):
        print(length_pair)