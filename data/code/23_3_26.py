def compare_sequences(seq1, seq2):
    for a, b in zip(seq1, seq2):
        if a > b:
            yield f'{a} is greater'
        elif a < b:
            yield f'{b} is smaller'
        else:
            yield 'Equal'

if __name__ == '__main__':
    sequence1 = [10, 20, 30, 40]
    sequence2 = [5, 25, 30, 35]
    
    for result in compare_sequences(sequence1, sequence2):
        print(result)