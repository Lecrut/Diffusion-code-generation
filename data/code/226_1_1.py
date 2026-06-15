def repeat_sequence(sequence, count):
    result = []
    for _ in range(count):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    seq1 = [1, 2]
    count1 = 3
    print(repeat_sequence(seq1, count1))
    seq2 = ('a', 'b')
    count2 = 2
    print(repeat_sequence(seq2, count2))
    seq3 = [10, 20, 30]
    count3 = 4
    print(repeat_sequence(seq3, count3))