def compare_values(seq1, seq2):
    for val1, val2 in zip(seq1, seq2):
        if val1 > val2:
            yield f'{val1} is greater'
        elif val1 < val2:
            yield f'{val2} is smaller'
        else:
            yield 'Equal'

if __name__ == '__main__':
    sequence1 = [5, 3, 9, 7]
    sequence2 = [4, 3, 8, 10]
    
    for result in compare_values(sequence1, sequence2):
        print(result)