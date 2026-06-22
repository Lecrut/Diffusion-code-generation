class SequenceProcessor:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def find_central_element(self):
        length = len(self.sequence)
        central_index = (length - 1) // 2
        return self.sequence[central_index]

if __name__ == '__main__':
    processor = SequenceProcessor([7, 3, 1, 8, 4, 9])
    print(processor.find_central_element())