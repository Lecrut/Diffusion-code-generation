class SequenceAccessor:

    def __init__(self, sequence):
        self.sequence = sequence

    def get_element(self, index):
        return self.sequence[index]
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    sample_tuple = (100, 200, 300, 400, 500)
    list_accessor = SequenceAccessor(sample_list)
    tuple_accessor = SequenceAccessor(sample_tuple)
    print(list_accessor.get_element(2))
    print(tuple_accessor.get_element(3))