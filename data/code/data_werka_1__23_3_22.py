def compare_pairs(seq1, seq2):
    for a, b in zip(seq1, seq2):
        if a > b:
            yield f'{a} is greater'
        elif a < b:
            yield f'{b} is smaller'
        else:
            yield 'Equal'

if __name__ == '__main__':
    sequence1 = [5, 3, 9, 7]
    sequence2 = [4, 3, 8, 10]
    
    for result in compare_pairs(sequence1, sequence2):
        print(result)