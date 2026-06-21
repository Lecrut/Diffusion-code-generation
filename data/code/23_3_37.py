def compare_values(seq1, seq2):
    COMPARISON_FORMAT = "{} is {}"
    
    def get_comparison(a, b):
        if a > b:
            return COMPARISON_FORMAT.format(a, 'greater')
        elif a < b:
            return COMPARISON_FORMAT.format(b, 'smaller')
        else:
            return 'Equal'
    
    for a, b in zip(seq1, seq2):
        yield get_comparison(a, b)

if __name__ == '__main__':
    sequence1 = [7, 3, 5, 9]
    sequence2 = [6, 3, 4, 8]
    for result in compare_values(sequence1, sequence2):
        print(result)