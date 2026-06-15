class SequenceRepeater:
    def repeat_sequence(self, sequence, count):
        if count <= 0:
            return tuple()
        return tuple(sequence * count)
if __name__ == '__main__':
    repeater = SequenceRepeater()
    seq1 = [1, 2]
    count1 = 3
    result1 = repeater.repeat_sequence(seq1, count1)
    print(f"Sequence: {seq1}, Count: {count1}, Result: {result1}")
    seq2 = ('a', 'b')
    count2 = 4
    result2 = repeater.repeat_sequence(seq2, count2)
    print(f"Sequence: {seq2}, Count: {count2}, Result: {result2}")
    seq3 = [10]
    count3 = 5
    result3 = repeater.repeat_sequence(seq3, count3)
    print(f"Sequence: {seq3}, Count: {count3}, Result: {result3}")
    seq4 = ()
    count4 = 2
    result4 = repeater.repeat_sequence(seq4, count4)
    print(f"Sequence: {seq4}, Count: {count4}, Result: {result4}")