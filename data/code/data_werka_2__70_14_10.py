class BoundaryRetriever:
    _MIN_LENGTH = 1

    @staticmethod
    def validate_input(data):
        if len(data) < BoundaryRetriever._MIN_LENGTH:
            raise ValueError("Input sequence must contain at least one element")
        return True

    def get_boundaries(self, sequence):
        self.validate_input(sequence)
        return sequence[0], sequence[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    retriever = BoundaryRetriever()
    result = retriever.get_boundaries(sample_data)
    print(result)