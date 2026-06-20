class SequenceHandler:
    def __init__(self):
        self.DEFAULT_VALUE = None

    @staticmethod
    def get_first_last(seq):
        if not seq:
            return (None, None)
        return (seq[0], seq[-1])

if __name__ == '__main__':
    handler = SequenceHandler()
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    empty_list = []
    empty_tuple = ()
    print(handler.get_first_last(sample_list))
    print(handler.get_first_last(sample_tuple))
    print(handler.get_first_last(empty_list))
    print(handler.get_first_last(empty_tuple))