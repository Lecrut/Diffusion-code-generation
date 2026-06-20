class SequenceHandler:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_first_and_last(self):
        if len(self.sequence) < 2:
            raise ValueError("Sequence must contain at least two elements.")
        return (self.sequence[0], self.sequence[-1])

if __name__ == '__main__':
    handler_list = SequenceHandler([1, 2, 3, 4, 5])
    try:
        print(handler_list.get_first_and_last())
    except ValueError as e:
        print(f"Error: {e}")

    handler_tuple = SequenceHandler((6, 7, 8, 9))
    try:
        print(handler_tuple.get_first_and_last())
    except ValueError as e:
        print(f"Error: {e}")