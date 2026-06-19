class SequenceAccessor:
    @staticmethod
    def get_element(sequence, index):
        return sequence[index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    sample_list = ['a', 'b', 'c', 'd', 'e']
    print(SequenceAccessor.get_element(sample_tuple, 2))
    print(SequenceAccessor.get_element(sample_list, 3))