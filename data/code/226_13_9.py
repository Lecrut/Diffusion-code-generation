class SequenceRepeater:
    SEQUENCE = [1, 2, 3]
    
    @staticmethod
    def repeat_sequence(num_repeats):
        result = []
        for _ in range(num_repeats):
            result.extend(SequenceRepeater.SEQUENCE)
        return result

if __name__ == '__main__':
    repeated_sequence = SequenceRepeater.repeat_sequence(5)
    print(repeated_sequence)