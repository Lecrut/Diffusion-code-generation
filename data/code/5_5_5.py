def compare_lengths(seq_a, seq_b):
    len_a = len(seq_a)
    len_b = len(seq_b)
    yield (len_a > len_b)
if __name__ == '__main__':
    sequence_a = list(range(100))
    sequence_b = list(range(50))
    result = next(compare_lengths(sequence_a, sequence_b))
    print(result)