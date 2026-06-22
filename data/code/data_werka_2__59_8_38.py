def find_middle_item(sequence):
    if not sequence:
        raise ValueError("The sequence is empty")
    middle_index = len(sequence) // 2
    return sequence[middle_index]

class SequenceHandler:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_middle_item(self):
        return find_middle_item(self.sequence)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    handler = SequenceHandler(sample_list)
    try:
        print(handler.get_middle_item())
    except ValueError as e:
        print(e)