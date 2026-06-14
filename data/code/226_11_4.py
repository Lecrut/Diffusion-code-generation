def repeat_sequence(sequence, n):
    return sequence * n
if __name__ == '__main__':
    seq1 = [1, 2]
    n1 = 3
    result1 = repeat_sequence(seq1, n1)
    print(f"Sequence: {seq1}, n: {n1}")
    print(f"Result: {result1}")
    seq2 = ('a', 'b')
    n2 = 2
    result2 = repeat_sequence(seq2, n2)
    print(f"Sequence: {seq2}, n: {n2}")
    print(f"Result: {list(result2)}")
    seq3 = [10]
    n3 = 5
    result3 = repeat_sequence(seq3, n3)
    print(f"Sequence: {seq3}, n: {n3}")
    print(f"Result: {result3}")