class SequenceRepeater:
    def repeat_sequence(self, sequence, count):
        if count <= 0:
            return []
        return sequence * count
if __name__ == '__main__':
    repeater = SequenceRepeater()
    sequence1 = [1, 2]
    count1 = 3
    result1 = repeater.repeat_sequence(sequence1, count1)
    print(f"Sequence: {sequence1}, Count: {count1}, Result: {result1}")
    sequence2 = ('a', 'b')
    count2 = 4
    result2 = repeater.repeat_sequence(sequence2, count2)
    print(f"Sequence: {sequence2}, Count: {count2}, Result: {result2}")
    sequence3 = [10]
    count3 = 5
    result3 = repeater.repeat_sequence(sequence3, count3)
    print(f"Sequence: {sequence3}, Count: {count3}, Result: {result3}")