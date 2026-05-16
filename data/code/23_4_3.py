def compare_sequences(seq1, seq2):
    for val1, val2 in zip(seq1, seq2):
        if val1 > val2:
            yield f"{val1} is greater"
        elif val1 < val2:
            yield f"{val1} is smaller"
        else:
            yield "Equal"
if __name__ == '__main__':
    sequence_a = [1, 5, 3, 8]
    sequence_b = [4, 2, 3, 9]
    results = list(compare_sequences(sequence_a, sequence_b))
    for result in results:
        print(result)