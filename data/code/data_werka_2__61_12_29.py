class SequenceElementFetcher:
    @staticmethod
    def get_element(sequence, index):
        if not isinstance(sequence, (list, tuple)):
            raise ValueError('Invalid sequence type')
        if index < 0 or index >= len(sequence):
            raise ValueError('Index out of range')
        return sequence[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    sample_tuple = (100, 200, 300, 400, 500)
    
    print(SequenceElementFetcher.get_element(sample_list, 2))
    print(SequenceElementFetcher.get_element(sample_tuple, 3))
    
    try:
        print(SequenceElementFetcher.get_element(sample_list, 10))
    except ValueError as e:
        print(e)
    
    try:
        print(SequenceElementFetcher.get_element('string', 2))
    except ValueError as e:
        print(e)