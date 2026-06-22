class SequenceRepeater:
    @staticmethod
    def repeat_sequence(sequence, count):
        return sequence * count

if __name__ == '__main__':
    sample_sequence = [7, 8, 9]
    sample_count = 4
    result = SequenceRepeater.repeat_sequence(sample_sequence, sample_count)
    print(result)