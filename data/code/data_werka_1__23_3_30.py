def compare_values(seq1, seq2):
    for a, b in zip(seq1, seq2):
        if a > b:
            yield 'A is greater'
        elif a < b:
            yield 'B is smaller'
        else:
            yield 'Equal'

if __name__ == '__main__':
    sequence1 = [1, 2, 3, 4]
    sequence2 = [2, 1, 4, 4]
    
    for result in compare_values(sequence1, sequence2):
        print(result)