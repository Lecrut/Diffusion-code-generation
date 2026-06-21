def compare_values(seq1, seq2):
    for a, b in zip(seq1, seq2):
        if a > b:
            yield 'A is greater'
        elif a < b:
            yield 'B is smaller'
        else:
            yield 'Equal'

if __name__ == '__main__':
    sequence1 = [7, 1, 5, 9]
    sequence2 = [3, 1, 8, 7]
    for result in compare_values(sequence1, sequence2):
        print(result)