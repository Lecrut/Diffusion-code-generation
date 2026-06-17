class SequenceRepeater:
    def repeat(self, sequence, count):
        if count <= 0:
            return []
        return sequence * count
if __name__ == '__main__':
    repeater = SequenceRepeater()
    sequence1 = [1, 2]
    count1 = 3
    result1 = repeater.repeat(sequence1, count1)
    print(f"Sequence: {sequence1}, Count: {count1}, Result: {result1}")
    sequence2 = ['a', 'b']
    count2 = 2
    result2 = repeater.repeat(sequence2, count2)
    print(f"Sequence: {sequence2}, Count: {count2}, Result: {result2}")
    sequence3 = [10, 20, 30]
    count3 = 0
    result3 = repeater.repeat(sequence3, count3)
    print(f"Sequence: {sequence3}, Count: {count3}, Result: {result3}")
    sequence4 = []
    count4 = 5
    result4 = repeater.repeat(sequence4, count4)
    print(f"Sequence: {sequence4}, Count: {count4}, Result: {result4}")