class SequenceHandler:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_first_element(self):
        try:
            return self.sequence[0]
        except (IndexError, TypeError):
            return None

if __name__ == '__main__':
    sample_list_handler = SequenceHandler([19, 20, 21])
    sample_tuple_handler = SequenceHandler((22, 23, 24))
    empty_list_handler = SequenceHandler([])
    empty_tuple_handler = SequenceHandler(())
    
    print(sample_list_handler.get_first_element())
    print(sample_tuple_handler.get_first_element())
    print(empty_list_handler.get_first_element())
    print(empty_tuple_handler.get_first_element())