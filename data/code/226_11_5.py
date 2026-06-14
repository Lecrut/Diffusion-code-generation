def repeat_sequence(sequence, n):
    return list(sequence * n)
if __name__ == '__main__':
    sequence1 = [1, 2]
    n1 = 3
    result1 = repeat_sequence(sequence1, n1)
    print(f"Sequence: {sequence1}, n: {n1}, Result: {result1}")
    sequence2 = ('a', 'b')
    n2 = 2
    result2 = repeat_sequence(sequence2, n2)
    print(f"Sequence: {sequence2}, n: {n2}, Result: {result2}")
    sequence3 = [10]
    n3 = 5
    result3 = repeat_sequence(sequence3, n3)
    print(f"Sequence: {sequence3}, n: {n3}, Result: {result3}")