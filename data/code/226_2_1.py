class SequenceRepeater:
    def repeat_sequence(self, sequence, repetitions):
        result = []
        for _ in range(repetitions):
            result.extend(sequence)
        return result
if __name__ == '__main__':
    repeater = SequenceRepeater()
    sample_sequence = [1, 2, 3]
    sample_repetitions = 2
    repeated_list = repeater.repeat_sequence(sample_sequence, sample_repetitions)
    print(repeated_list)