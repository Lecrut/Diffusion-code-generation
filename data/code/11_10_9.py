class SequenceProcessor:
    def __init__(self, sequence):
        self.data = sequence

    def get_last_element(self):
        if not self.data:
            raise IndexError("list index out of range")
        return self.data[-1]

if __name__ == '__main__':
    sample_data = [7, 9, 13, 21, 34]
    processor = SequenceProcessor(sample_data)
    result = processor.get_last_element()
    print(result)