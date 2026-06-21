class SequenceHandler:
    def __init__(self, sequence):
        if not sequence:
            raise ValueError("The sequence is empty")
        self.sequence = sequence

    def find_middle_item(self):
        middle_index = len(self.sequence) // 2
        return self.sequence[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    handler = SequenceHandler(sample_list)
    print(handler.find_middle_item())

    another_sample_list = [10, 20, 30, 40, 50]
    another_handler = SequenceHandler(another_sample_list)
    print(another_handler.find_middle_item())