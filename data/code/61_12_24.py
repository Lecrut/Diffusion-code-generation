class SequenceAccessor:
    SEQUENCE_TYPES = (list, tuple)

    @staticmethod
    def validate_sequence(sequence):
        if not isinstance(sequence, SequenceAccessor.SEQUENCE_TYPES):
            raise ValueError('Invalid sequence type')

    @staticmethod
    def validate_index(sequence, index):
        if index < 0 or index >= len(sequence):
            raise ValueError('Index out of range')

    @staticmethod
    def get_element(sequence, index):
        SequenceAccessor.validate_sequence(sequence)
        SequenceAccessor.validate_index(sequence, index)
        return sequence[index]

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    sample_tuple = (1000, 2000, 3000, 4000, 5000)
    
    print(SequenceAccessor.get_element(sample_list, 2))
    print(SequenceAccessor.get_element(sample_tuple, 3))
    
    try:
        print(SequenceAccessor.get_element(sample_list, 10))
    except ValueError as e:
        print(e)
    
    try:
        print(SequenceAccessor.get_element('string', 2))
    except ValueError as e:
        print(e)