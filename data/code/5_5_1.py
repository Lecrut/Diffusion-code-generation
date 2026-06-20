import itertools

def compare_lengths():
    sequences_a = (len(f"sequence_a_{i}") for i in range(5))
    sequences_b = (len(f"sequence_b_{i}") for i in range(5))
    for len_a, len_b in itertools.zip_longest(sequences_a, sequences_b, fillvalue=0):
        if len_a > len_b:
            yield 1
        elif len_a < len_b:
            yield -1
        else:
            yield 0

if __name__ == '__main__':
    results = list(compare_lengths())
    print(results)