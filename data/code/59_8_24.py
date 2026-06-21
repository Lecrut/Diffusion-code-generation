class SequenceHandler:
    def __init__(self, sequence):
        self.sequence = sequence

    def find_middle_item(self):
        if not self.sequence:
            raise ValueError("The sequence is empty")
        middle_index = len(self.sequence) // 2
        return self.sequence[middle_index]

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    handler = SequenceHandler(sample_list)
    print(handler.find_middle_item())