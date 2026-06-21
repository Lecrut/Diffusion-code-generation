def compare_values(seq1, seq2):
    comparison_map = {
        'greater': '{} is greater',
        'smaller': '{} is smaller',
        'equal': 'Equal'
    }
    
    for a, b in zip(seq1, seq2):
        if a > b:
            yield comparison_map['greater'].format(a)
        elif a < b:
            yield comparison_map['smaller'].format(b)
        else:
            yield comparison_map['equal']

if __name__ == '__main__':
    sequence1 = [7, 1, 4, 6]
    sequence2 = [3, 2, 4, 5]
    for result in compare_values(sequence1, sequence2):
        print(result)