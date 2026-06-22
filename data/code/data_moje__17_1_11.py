class SequenceProcessor:
    def __init__(self, sequence):
        self.sequence = sequence
        self._length = len(sequence)

    def retrieve_final_element(self):
        if self._length == 0:
            raise ValueError("Cannot retrieve from an empty sequence")
        index = self._length - 1
        return self.sequence[index]

if __name__ == '__main__':
    data = [7, 14, 21, 28, 35]
    processor = SequenceProcessor(data)
    print(processor.retrieve_final_element())