class SequenceHandler:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_last_element(self):
        if not self.sequence:
            raise IndexError("Cannot retrieve last element from an empty sequence")
        return self.sequence[-1]

if __name__ == '__main__':
    sample_sequence = [100, 200, 300, 400, 500]
    handler = SequenceHandler(sample_sequence)
    print(handler.get_last_element())