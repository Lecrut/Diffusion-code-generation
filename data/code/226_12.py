class SequenceRepeater:
    def generate(self, sequence, count):
        for _ in range(count):
            yield from sequence
if __name__ == '__main__':
    repeater = SequenceRepeater()
    sample_sequence = [1, 2]
    repetition_count = 3
    result = list(repeater.generate(sample_sequence, repetition_count))
    print(result)