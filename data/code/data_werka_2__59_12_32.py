class CentralItemRetriever:
    EMPTY_SEQUENCE_ERROR = 'The sequence is empty'
    
    @staticmethod
    def get_central_item(sequence):
        if not sequence:
            raise ValueError(CentralItemRetriever.EMPTY_SEQUENCE_ERROR)
        length = len(sequence)
        mid_index = length // 2
        if length % 2 == 0:
            return (sequence[mid_index - 1] + sequence[mid_index]) / 2
        else:
            return sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [3, 6, 9, 12, 15]
    sample_sequence_even = [4, 8, 12, 16, 20, 24]
    print(CentralItemRetriever.get_central_item(sample_sequence_odd))
    print(CentralItemRetriever.get_central_item(sample_sequence_even))