class SequenceHandler:
    EMPTY_SEQUENCE = None

    @staticmethod
    def get_central_item(sequence):
        if not sequence:
            return SequenceHandler.EMPTY_SEQUENCE
        length = len(sequence)
        mid_index = length // 2
        if length % 2 == 0:
            return (sequence[mid_index - 1], sequence[mid_index])
        else:
            return sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_1 = [7, 14, 21, 28, 35]
    sample_sequence_2 = [1000, 2000, 3000, 4000, 5000, 6000]
    sample_sequence_3 = []
    print(SequenceHandler.get_central_item(sample_sequence_1))
    print(SequenceHandler.get_central_item(sample_sequence_2))
    print(SequenceHandler.get_central_item(sample_sequence_3))