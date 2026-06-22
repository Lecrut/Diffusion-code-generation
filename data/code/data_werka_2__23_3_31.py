def compare_pairs(seq1, seq2):
    for a, b in zip(seq1, seq2):
        if a > b:
            yield f'{a} is greater'
        elif a < b:
            yield f'{b} is smaller'
        else:
            yield 'Equal'

if __name__ == '__main__':
    seq1 = [10, 20, 30]
    seq2 = [5, 20, 25]
    
    for result in compare_pairs(seq1, seq2):
        print(result)