def repeat_sequence(sequence, n):
    return list(sequence * n)
if __name__ == '__main__':
    seq1 = [1, 2]
    n1 = 3
    result1 = repeat_sequence(seq1, n1)
    print(result1)
    seq2 = ('a', 'b')
    n2 = 2
    result2 = repeat_sequence(seq2, n2)
    print(result2)
    seq3 = [10]
    n3 = 5
    result3 = repeat_sequence(seq3, n3)
    print(result3)