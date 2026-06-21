class SequenceUtils:
    INDEX_OFFSET = -1

    @staticmethod
    def retrieve_last(sequence):
        if not sequence:
            raise ValueError("Sequence cannot be empty")
        return sequence[SequenceUtils.INDEX_OFFSET]

if __name__ == '__main__':
    sample_data = [5, 12, 99, 34, 88]
    print(SequenceUtils.retrieve_last(sample_data))