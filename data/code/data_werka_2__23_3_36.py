def compare_pairs(seq1, seq2):
    for a, b in zip(seq1, seq2):
        if a > b:
            yield 'A is greater'
        elif a < b:
            yield 'B is smaller'
        else:
            yield 'Equal'

if __name__ == '__main__':
    seq1 = [5, 3, 8, 7]
    seq2 = [4, 3, 6, 9]
    
    for result in compare_pairs(seq1, seq2):
        print(result)