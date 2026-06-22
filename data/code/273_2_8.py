import time

class SequenceRepeater:
    def repeat_sequence(self, sequence):
        for _ in range(3):
            print(sequence)
            time.sleep(1)

if __name__ == '__main__':
    repeater = SequenceRepeater()
    sequence1 = [1, 2]
    repeater.repeat_sequence(sequence1)
    sequence2 = ['a', 'b']
    repeater.repeat_sequence(sequence2)
    sequence3 = [10, 20, 30]
    repeater.repeat_sequence(sequence3)