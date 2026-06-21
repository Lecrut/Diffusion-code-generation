def compare_values(seq1, seq2):
    for value1, value2 in zip(seq1, seq2):
        if value1 > value2:
            yield f'{value1} is greater'
        elif value1 < value2:
            yield f'{value2} is smaller'
        else:
            yield 'Equal'

if __name__ == '__main__':
    sequence_a = [7, 1, 5, 9]
    sequence_b = [3, 4, 5, 6]
    for comparison_result in compare_values(sequence_a, sequence_b):
        print(comparison_result)