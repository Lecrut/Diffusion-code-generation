class SequenceHandler:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_first_element(self):
        return self.sequence[0] if self.sequence else None

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    empty_list = []
    empty_tuple = ()

    handler_list = SequenceHandler(sample_list)
    handler_tuple = SequenceHandler(sample_tuple)
    handler_empty_list = SequenceHandler(empty_list)
    handler_empty_tuple = SequenceHandler(empty_tuple)

    print(handler_list.get_first_element())
    print(handler_tuple.get_first_element())
    print(handler_empty_list.get_first_element())
    print(handler_empty_tuple.get_first_element())