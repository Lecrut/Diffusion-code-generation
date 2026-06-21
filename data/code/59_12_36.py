class CentralItemRetriever:
    EMPTY_SEQUENCE_ERROR = 'The sequence is empty'

    @staticmethod
    def calculate_central_index(length):
        return length // 2

    def __init__(self, sequence):
        if not sequence:
            raise ValueError(self.EMPTY_SEQUENCE_ERROR)
        self.sequence = sequence

    def get_central_item(self):
        length = len(self.sequence)
        mid_index = self.calculate_central_index(length)
        if length % 2 == 0:
            return (self.sequence[mid_index - 1] + self.sequence[mid_index]) / 2
        else:
            return self.sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [3, 6, 9, 12, 15]
    sample_sequence_even = [4, 8, 12, 16, 20, 24]
    retriever_odd = CentralItemRetriever(sample_sequence_odd)
    retriever_even = CentralItemRetriever(sample_sequence_even)
    print(retriever_odd.get_central_item())
    print(retriever_even.get_central_item())