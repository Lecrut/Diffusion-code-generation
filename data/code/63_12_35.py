class SequenceUtils:
    @staticmethod
    def get_first_element(sequence):
        return sequence[0] if sequence else None

if __name__ == '__main__':
    sample_list = [25, 26, 27]
    sample_tuple = (28, 29, 30)
    empty_list = []
    empty_tuple = ()
    print(SequenceUtils.get_first_element(sample_list))
    print(SequenceUtils.get_first_element(sample_tuple))
    print(SequenceUtils.get_first_element(empty_list))
    print(SequenceUtils.get_first_element(empty_tuple))