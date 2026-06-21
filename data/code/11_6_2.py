class TailAccessError(Exception):
    def __init__(self, index):
        self.index = index
        super().__init__(f"Index -1 is invalid for empty sequence at index {index}")

def retrieve_tail_element(sequence):
    if not sequence:
        raise TailAccessError(0)
    return sequence[-1]

if __name__ == '__main__':
    data_sequence = [10, 20, 30, 40, 50]
    value = retrieve_tail_element(data_sequence)
    print(value)
    empty_sequence = []
    try:
        retrieve_tail_element(empty_sequence)
    except TailAccessError as err:
        print(err.message)