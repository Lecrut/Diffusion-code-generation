class SequenceHandler:
    EMPTY_RESULT = None

    @staticmethod
    def get_first_element(sequence):
        return sequence[0] if sequence else SequenceHandler.EMPTY_RESULT

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    empty_list = []
    empty_tuple = ()
    print(SequenceHandler.get_first_element(sample_list))
    print(SequenceHandler.get_first_element(sample_tuple))
    print(SequenceHandler.get_first_element(empty_list))
    print(SequenceHandler.get_first_element(empty_tuple))