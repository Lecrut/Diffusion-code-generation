class SequenceTail:
    EMPTY_MSG = "Cannot retrieve last element from empty sequence"

    @staticmethod
    def validate(seq):
        if len(seq) == 0:
            raise IndexError(SequenceTail.EMPTY_MSG)

    @staticmethod
    def get_last(sequence):
        SequenceTail.validate(sequence)
        return sequence[-1]

if __name__ == '__main__':
    data = [100, 200, 300]
    print(SequenceTail.get_last(data))