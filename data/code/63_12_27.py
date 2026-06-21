class SafeSequenceAccessor:
    def __init__(self, sequence):
        self.sequence = sequence

    def get_first_element(self):
        if isinstance(self.sequence, (list, tuple)) and len(self.sequence) > 0:
            return self.sequence[0]
        return None

if __name__ == '__main__':
    sample_list_accessor = SafeSequenceAccessor([25, 26, 27])
    sample_tuple_accessor = SafeSequenceAccessor((28, 29, 30))
    empty_list_accessor = SafeSequenceAccessor([])
    empty_tuple_accessor = SafeSequenceAccessor(())
    invalid_input_accessor = SafeSequenceAccessor("not a sequence")

    print(sample_list_accessor.get_first_element())
    print(sample_tuple_accessor.get_first_element())
    print(empty_list_accessor.get_first_element())
    print(empty_tuple_accessor.get_first_element())
    print(invalid_input_accessor.get_first_element())